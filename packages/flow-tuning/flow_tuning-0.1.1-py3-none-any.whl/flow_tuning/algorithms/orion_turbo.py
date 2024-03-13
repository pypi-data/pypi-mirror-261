from abc import ABC
from abc import abstractmethod
import heapq
from typing import Dict, Generic, List, Literal, NamedTuple, Optional, override, Set, Tuple, TypeVar  # NOQA

from matplotlib import pyplot as plt  # NOQA
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit

from flow_tuning.algorithms.base import BaseAlgorithm
from flow_tuning.providers.base import BaseProvider
from flow_tuning.providers.base import FunctionConfig
from flow_tuning.providers.base import WorkflowDescription
from flow_tuning.providers.base import WorkflowInvocationResult
from flow_tuning.providers.base import WorkflowStepDescription
from flow_tuning.providers.base import WorkflowStepInvocationResult
from flow_tuning.utils.console import console

T = TypeVar("T")
C = TypeVar("C")


class Model(ABC, Generic[T, C]):

  @abstractmethod
  def feed(self, config: C, data: List[T]) -> None:
    pass

  @abstractmethod
  def train(self) -> None:
    pass

  @abstractmethod
  def estimate(self, config: C) -> Tuple[float, float]:
    pass


class ModelConfig(NamedTuple):
  provider: BaseProvider
  static: Optional[bool] = True


class WorkflowModel(Model[WorkflowInvocationResult, Dict[str, FunctionConfig]]):

  def __init__(
      self, config: ModelConfig, description: WorkflowDescription
  ) -> None:
    super().__init__()
    self.config = config
    self.workflow_id = description.workflow_id
    self.description: WorkflowDescription = description
    self.steps: Dict[str, "WorkflowStepModel"] = {}
    for step in description.steps:
      self.steps[step.step_id] = createStepModel(step.type, config, step)

  @override
  def feed(self, config, data):
    for invocation in data:
      for i, step in enumerate(invocation.steps):
        if step.step_id != self.description.steps[i].step_id:
          raise ValueError(
              f"Step result mismatch for workflow {self.workflow_id} step {self.description.steps[i].step_id}, got {step.step_id}"
          )
        self.steps[step.step_id].feed(config, [step])

  @override
  def train(self):
    for step in self.steps.values():
      step.train()

  @override
  def estimate(self, config):
    latency_and_costs = [step.estimate(config) for step in self.steps.values()]
    return sum(latency for latency, _ in latency_and_costs
              ), sum(cost for _, cost in latency_and_costs)


class WorkflowStepModel(
    Model[WorkflowStepInvocationResult, Dict[str, FunctionConfig]]
):

  def __init__(
      self, config: ModelConfig, description: WorkflowStepDescription
  ) -> None:
    super().__init__()
    self.step_id = description.step_id
    self.config = config
    self.description = description


class WorkflowFixedStepModel(WorkflowStepModel):

  def __init__(
      self, config: ModelConfig, description: WorkflowStepDescription
  ) -> None:
    super().__init__(config, description)
    self.mean_latency = 0
    self.durations: List[float] = []

  @override
  def feed(self, config, data) -> None:
    self.durations += [invocation.duration for invocation in data]

  @override
  def train(self):
    durations = np.array(self.durations)
    self.mean_latency = float(np.mean(durations))

  @override
  def estimate(self, config):
    return self.mean_latency, 0


class WorkflowFunctionStepModel(WorkflowStepModel):

  def __init__(
      self, config: ModelConfig, description: WorkflowStepDescription
  ) -> None:
    super().__init__(config, description)
    if not description.function_id:
      raise ValueError(
          f"Function step {description.step_id} missing function_id"
      )
    self.function_id = description.function_id
    self.records: List[Tuple[FunctionConfig, float]] = []
    self.overheads: List[float] = []
    self.overhead = 0

  @override
  def feed(self, config, data) -> None:
    current_config = config[self.function_id]
    for invocation in data:
      self.records += [(current_config, invocation.task_duration)]
      overhead = invocation.duration - invocation.task_duration - invocation.init_duration
      self.overheads += [overhead]

  @staticmethod
  def _model_func(m, a0, a1, a2, a3):
    return a0 / np.minimum(m, a1) + a2 / m + a3 / np.log(m)

  @override
  def train(self):
    self.overhead = float(np.mean(self.overheads))
    m = np.array([config.memory for config, _ in self.records])
    t = np.array([duration for _, duration in self.records])
    df = pd.DataFrame({'memory': m, 'time': t})
    average_times = df.groupby('memory').time.mean().reset_index()
    self.m_unique = average_times['memory'].values
    self.t_unique = average_times['time'].values
    if not self.config.static:
      popt, pcov = curve_fit(
          self._model_func,
          self.m_unique,
          self.t_unique,
          maxfev=10000,
          bounds=([0, 0, 0, 0], [np.inf, np.inf, np.inf, np.inf])
      )
      self.args = popt
      console.log(f"Function {self.function_id} model parameters: {popt}")

  @override
  def estimate(self, config):
    current_config = config[self.function_id]
    if self.config.static:
      index = self.m_unique.searchsorted(current_config.memory)
      latency = self.t_unique[index]
    else:
      latency = self._model_func(current_config.memory, *self.args)
    cost = self.config.provider.get_function_cost(
        self.function_id, current_config, latency
    )
    return self.overhead + latency, cost


class WorkflowParallelStepModel(WorkflowStepModel):

  def __init__(
      self, config: ModelConfig, description: WorkflowStepDescription
  ) -> None:
    super().__init__(config, description)

    if not description.branches:
      raise ValueError(f"Parallel step {description.step_id} missing branches")
    self.branches = {
        branch_id: WorkflowModel(config, branch)
        for branch_id, branch in description.branches.items()
    }
    self.overheads: List[float] = []

  @override
  def feed(self, config, data) -> None:
    for item in data:
      if not item.branched_results:
        raise ValueError(
            f"Parallel step {self.step_id} missing branched results"
        )
      for branch_id, invocation in item.branched_results.items():
        self.branches[branch_id].feed(config, [invocation])
      # Sub-latency is not related to function config
      latency = max(
          sum(step.duration
              for step in item.branched_results[branch_id].steps)
          for branch_id in self.branches
      )
      overhead = item.duration - latency
      self.overheads += [overhead]

  @override
  def train(self):
    for branch in self.branches.values():
      branch.train()
    self.overhead = float(np.mean(self.overheads))

  @override
  def estimate(self, config: Dict[str, FunctionConfig]):
    sub_results = [branch.estimate(config) for branch in self.branches.values()]
    latency = max(latency for latency, _ in sub_results)
    cost = sum(cost for _, cost in sub_results)
    return self.overhead + latency, cost


class WorkflowMapStepModel(WorkflowStepModel):

  def __init__(
      self, config: ModelConfig, description: WorkflowStepDescription
  ) -> None:
    super().__init__(config, description)

    if not description.workflow:
      raise ValueError(f"Map step {description.step_id} missing workflow")
    self.processor = WorkflowModel(config, description.workflow)
    self.overheads: List[float] = []
    self.iterations: List[float] = []

  @override
  def feed(self, config, data):
    for item in data:
      if not item.mapped_results:
        raise ValueError(f"Map step {self.step_id} missing mapped results")
      self.processor.feed(config, item.mapped_results)
      latency = max(
          sum(step.duration
              for step in iteration.steps)
          for iteration in item.mapped_results
      )
      overhead = item.duration - latency
      self.overheads += [overhead]
      self.iterations += [len(item.mapped_results)]

  @override
  def train(self):
    self.processor.train()
    self.overhead = float(np.mean(self.overheads))
    self.iteration = float(np.mean(self.iterations))
    console.log(
        f"WARN: assuming map state will concurrently execute all iterations"
    )

  @override
  def estimate(self, config):
    latency, cost = self.processor.estimate(config)
    return self.overhead + latency, cost * self.iteration


def createStepModel(
    type: Literal["fixed", "function", "branch", "parallel", "map"],
    config: ModelConfig, description: WorkflowStepDescription
) -> WorkflowStepModel:
  match type:
    case "fixed":
      return WorkflowFixedStepModel(config, description)
    case "function":
      return WorkflowFunctionStepModel(config, description)
    case "parallel":
      return WorkflowParallelStepModel(config, description)
    case "map":
      return WorkflowMapStepModel(config, description)
    case _:
      raise ValueError(f"Unsupported step type {type}")


def summarize_state(state: Dict[str, FunctionConfig]):
  configs = [(k.split(':')[-1], v.memory) for k, v in state.items()]
  return ' '.join(f"{func_id}={memory}" for func_id, memory in configs)


def visualize_function(model: WorkflowFunctionStepModel):
  console.log(f"Visualizing function step {model.step_id}")
  memory_values = [int(config.memory) for config, _ in model.records]
  memory_values = list(set(memory_values))
  memory_values = sorted(memory_values)
  memory_to_results: Dict[int, Tuple[int, float]] = {}
  for config, results in model.records:
    total, sum = memory_to_results.get(int(config.memory), (0, 0))
    memory_to_results[int(config.memory)] = (total + 1, sum + results)
  console.log({
      mem: sum / total for mem, (total, sum) in memory_to_results.items()
  })
  memory = np.array(memory_values, dtype=np.float64)
  latency_values = [sum / total for total, sum in memory_to_results.values()]
  latency = np.array(latency_values, dtype=np.float64)
  cost_values = [
      model.config.provider.get_function_cost(
          model.function_id, FunctionConfig(memory=m), l
      ) for m, l in zip(memory, latency)
  ]
  cost = np.array(cost_values, dtype=np.float64)
  memory_line = np.linspace(min(memory), max(memory), 100)
  # coeffs_latency = np.polyfit(memory, latency, 1)
  # p_latency = np.poly1d(coeffs_latency)
  # estimated_latency_line = p_latency(memory_line)
  # vec_cost_fn = np.vectorize(cost_fn)
  # estimated_cost_line = vec_cost_fn(memory_line, estimated_latency_line)
  if model.config.static:
    from scipy.interpolate import make_interp_spline
    latency_line = make_interp_spline(memory, latency)(memory_line)
    cost_line = make_interp_spline(memory, cost)(memory_line)
  else:
    latency_line = model._model_func(memory_line, *model.args)
    cost_fn = lambda m, l: model.config.provider.get_function_cost(
        model.function_id, FunctionConfig(memory=m), l
    )
    cost_line = np.vectorize(cost_fn)(memory_line, latency_line)
    a0, a1, a2, a3 = model.args
    console.log(
        f"Estimated latency formula: lat = {a0} / min(m, {a1}) + {a2} / m + {a3} / log(m)"
    )
  fig, ax1 = plt.subplots()
  color = 'tab:red'
  ax1.set_xlabel('Memory (MB)')
  ax1.set_ylabel('Cost (USD)', color=color)
  ax1.scatter(memory, cost, color=color, label='Cost')
  ax1.tick_params(axis='y', labelcolor=color)
  ax1.plot(
      memory_line,
      cost_line,
      color=color,
      linestyle='--',
      label='Estimated cost line'
  )
  ax2 = ax1.twinx()
  color = 'tab:blue'
  ax2.set_ylabel('Latency (ms)', color=color)
  ax2.scatter(memory, latency, color=color, label='Latency')
  ax2.tick_params(axis='y', labelcolor=color)
  ax2.plot(
      memory_line,
      latency_line,
      color=color,
      linestyle='--',
      label='Estimated latency line'
  )

  fig.tight_layout()
  plt.title(f'Memory - Cost - Latency for {model.step_id}')

  # plt.show()


def visualize(model: WorkflowModel, root=True):
  for step in model.steps.values():
    if isinstance(step, WorkflowFunctionStepModel):
      visualize_function(step)
    elif isinstance(step, WorkflowParallelStepModel):
      for branch in step.branches.values():
        visualize(branch, False)
    elif isinstance(step, WorkflowMapStepModel):
      visualize(step.processor, False)
  if root:
    plt.show()


class OrionTurboAlgorithm(BaseAlgorithm):

  @override
  def optimize_function(self, input, provider, function_id, dispatched_results):
    raise NotImplementedError("Orion can't optimize functions")

  @override
  def optimize_workflow(
      self, input, provider, workflow_id, description, dispatched_results
  ):
    static = input.get('static', False)
    step_size = input.get('step_size', 0 if static else None)
    if not step_size:
      raise ValueError("Step size is required for non-static tuning")

    model_config = ModelConfig(provider=provider, static=static)
    model = WorkflowModel(model_config, description)
    for config, data in dispatched_results:
      model.feed(config, data)
    model.train()
    visualize(model)

    latency_goal = input['objectives']['latency']['max']
    console.log(f"Targeting latency for {latency_goal} ms")

    configs_sets: Dict[str, Set[FunctionConfig]] = {}
    for config, _ in dispatched_results:
      for func_id, func_config in config.items():
        if func_id not in configs_sets:
          configs_sets[func_id] = set()
        configs_sets[func_id].add(func_config)

    function_configs: Dict[str, List[FunctionConfig]] = {
        func_id: sorted(func_configs, key=lambda c: c.memory)
        for func_id, func_configs in configs_sets.items()
    }
    state = {
        func_id: function_configs[0]
        for func_id, function_configs in function_configs.items()
    }
    latency_max, latency_max_cost = model.estimate(state)
    state = {
        func_id: function_configs[-1]
        for func_id, function_configs in function_configs.items()
    }
    latency_min, latency_min_cost = model.estimate(state)
    console.log(f"Latency range: {latency_min}ms - {latency_max}ms")
    console.log(f"Cost         : {latency_min_cost} - {latency_max_cost}")
    if latency_goal < latency_min:
      console.log(
          f"WARNING: latency goal is lower than minimum latency, returning minimum configuration"
      )
      return state

    best_config_latency, best_config_cost = model.estimate(state)
    best_config = state

    if static:
      static_queue: List[Tuple[int,
                               List[int]]] = [(0, [0] * len(function_configs))]
      keys = list(function_configs.keys())
      total = 0
      while static_queue:
        n, indexes = heapq.heappop(static_queue)
        if n >= len(function_configs):
          total += 1
          state = {
              func_id: function_configs[i]
              for i, (func_id, function_configs
                     ) in zip(indexes, function_configs.items())
          }
          latency, cost = model.estimate(state)
          if latency < latency_goal:
            if cost < best_config_cost:
              best_config = state
              best_config_latency = latency
              best_config_cost = cost
          continue
        for next_index in range(len(function_configs[keys[n]])):
          next_indexes = indexes.copy()
          next_indexes[n] = next_index
          static_queue += [(n + 1, next_indexes)]
      console.log(f"Explored {total} configurations")

    else:
      state = {
          func_id: function_configs[0]
          for func_id, function_configs in function_configs.items()
      }
      queue: List[Tuple[float, Dict[str, FunctionConfig]]] = [(0, state)]
      while queue:
        _, state = heapq.heappop(queue)
        console.log(f"Exploring state: {summarize_state(state)}")
        for func_id in state:
          next_state = state.copy()
          if static:
            options = function_configs[func_id]
            index = options.index(state[func_id])
            if index < len(options) - 1:
              next_state[func_id] = options[index + 1]
            else:
              continue
          else:
            next_state[func_id] = FunctionConfig(
                memory=state[func_id].memory + step_size
            )
          latency, cost = model.estimate(next_state)
          if latency <= latency_goal:
            console.log(f"Valid config : {summarize_state(next_state)}")
            console.log(f"Latency      : {latency}ms")
            console.log(f"Cost         : {cost}")
            return next_state
          priority = latency * cost
          heapq.heappush(queue, (priority, next_state))

    console.log(f"Best config  : {summarize_state(best_config)}")
    console.log(f"Latency      : {best_config_latency}ms")
    console.log(f"Cost         : {best_config_cost}")
    return best_config
