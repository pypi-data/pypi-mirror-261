from typing import Any, Callable, Dict, List, override, Tuple

from matplotlib import pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

from flow_tuning.algorithms.base import BaseAlgorithm
from flow_tuning.algorithms.base import FunctionDispatchedResults
from flow_tuning.providers.base import BaseProvider
from flow_tuning.providers.base import FunctionConfig
from flow_tuning.providers.base import FunctionInvocationResult
from flow_tuning.utils.console import console


def visualize(
    # (memory, latency, cost)
    points: List[Tuple[int, float, float]],
    cost_fn: Callable[[float, float], float]
):
  memory = np.array([point[0] for point in points], dtype=np.float64)
  latency = np.array([point[1] for point in points], dtype=np.float64)
  cost = np.array([point[2] for point in points], dtype=np.float64)
  memory_line = np.linspace(min(memory), max(memory), 100)
  # coeffs_latency = np.polyfit(memory, latency, 1)
  # p_latency = np.poly1d(coeffs_latency)
  # estimated_latency_line = p_latency(memory_line)
  # vec_cost_fn = np.vectorize(cost_fn)
  # estimated_cost_line = vec_cost_fn(memory_line, estimated_latency_line)
  latency_line = make_interp_spline(memory, latency)(memory_line)
  cost_line = make_interp_spline(memory, cost)(memory_line)
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
  plt.title('Memory - Cost - Latency')

  plt.show()


class PowerTuningAlgorithm(BaseAlgorithm):

  @override
  def optimize_function(
      self, input: Dict[str, Any], provider: BaseProvider, function_id: str,
      dispatched_results: FunctionDispatchedResults
  ):
    weight = input.get('weight', None)
    if not weight:
      raise ValueError("Weight is required for Power Tuning")
    console.log("Weight:", weight)
    memory_values = [result[0].memory for result in dispatched_results]
    memory_values = sorted(memory_values)
    memory_to_results: Dict[int, List[FunctionInvocationResult]] = {}
    for config, results in dispatched_results:
      memory_to_results[int(config.memory)] = results
    # (memory, avg_duration, avg_cost)
    points: List[Tuple[int, float, float]] = []
    for memory in memory_values:
      results = memory_to_results[int(memory)]
      total_duration = 0.0
      total_cost = 0.0
      for result in results:
        total_duration += result.task_duration
        total_cost += provider.get_function_cost(
            function_id, FunctionConfig(memory=memory), result.task_duration
        )
      avg_duration = total_duration / len(results)
      avg_cost = total_cost / len(results)
      points.append((int(memory), avg_duration, avg_cost))
    console.log("Calculated points:")
    console.log(points)

    def get_cost(mem: float, lat: float) -> float:
      return provider.get_function_cost(
          function_id, FunctionConfig(memory=mem), lat
      )

    visualize(list(map(lambda x: (x[0], x[1], x[2]), points)), get_cost)
    max_duration = max(map(lambda x: x[1], points))
    max_cost = max(map(lambda x: x[2], points))
    sorted_points = sorted(
        points,
        key=lambda x: ((x[1] * (1 - weight) / max_duration) +
                       (x[2] * weight / max_cost))
    )
    console.log("Best point found:")
    console.log(sorted_points[0])
    _, best_duration, best_cost = sorted_points[0]
    return FunctionConfig(memory=sorted_points[0][0])

  @override
  def optimize_workflow(
      self, input, provider, workflow_id, description, dispatched_results
  ) -> Dict[str, FunctionConfig]:
    raise NotImplementedError("Power Tuning can't optimize workflows")
