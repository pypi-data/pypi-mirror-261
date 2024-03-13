import asyncio
from typing import Any, Dict, List, Literal, NamedTuple, Tuple

from flow_tuning.algorithms.base import BaseAlgorithm
from flow_tuning.generators.base import BaseGenerator
from flow_tuning.providers.base import BaseProvider
from flow_tuning.providers.base import FunctionConfig
from flow_tuning.providers.base import WorkflowDescription
from flow_tuning.providers.base import WorkflowInvocationResult
from flow_tuning.utils.console import console
from flow_tuning.utils.module_loader import load_class


class WorkflowTuningInitializerInput(NamedTuple):
  provider: str
  workflow_id: str
  description: WorkflowDescription
  function_configs: Dict[str, FunctionConfig]


async def initialize(input: WorkflowTuningInitializerInput) -> None:
  Provider = load_class(BaseProvider, input.provider)
  provider = Provider()  # type: ignore
  for function_id, function_config in input.function_configs.items():
    await provider.configure_function(
        function_id=function_id, qualifier="FT-LATEST", config=function_config
    )
    console.log(f"Function {function_id} Flow Tuning alias configured")


class WorkflowTuningExecutorInput(NamedTuple):
  provider: str
  workflow_id: str
  description: WorkflowDescription
  generator: str
  generator_input: Dict[str, Any]
  invocation_mode: Literal['serial', 'parallel']


class WorkflowTuningExecutorOutput(NamedTuple):
  results: List[WorkflowInvocationResult]


async def execute(
    input: WorkflowTuningExecutorInput
) -> WorkflowTuningExecutorOutput:
  Provider = load_class(BaseProvider, input.provider)
  provider = Provider()  # type: ignore
  Generator = load_class(BaseGenerator, input.generator)
  generator = Generator()  # type: ignore
  results: List[WorkflowInvocationResult] = []
  batch_count = 0
  async for batch in generator.generate_batch(input.generator_input):
    batch_count += 1
    console.log(
        f"Executing batch={batch_count}(x{len(batch)})"
        f" in {input.invocation_mode}"
    )
    if input.invocation_mode == 'serial':
      for payload in batch:
        result = await provider.invoke_workflow(
            workflow_id=input.workflow_id,
            description=input.description,
            payload=payload
        )
        results.append(result)
    elif input.invocation_mode == 'parallel':
      tasks = map(
          lambda payload: provider.invoke_workflow(
              workflow_id=input.workflow_id,
              description=input.description,
              payload=payload
          ), batch
      )
      results.extend(await asyncio.gather(*tasks))
  return WorkflowTuningExecutorOutput(results)


class WorkflowTuningDispatcherInput(NamedTuple):
  provider: str
  workflow_id: str
  function_configs: Dict[str, List[FunctionConfig]]
  generator: str
  generator_input: Dict[str, Any]
  invocation_mode: Literal['serial', 'parallel']


class WorkflowTuningDispatcherOutput(NamedTuple):
  description: WorkflowDescription
  results: List[Tuple[Dict[str, FunctionConfig], WorkflowTuningExecutorOutput]]


async def dispatch(
    input: WorkflowTuningDispatcherInput
) -> WorkflowTuningDispatcherOutput:
  Provider = load_class(BaseProvider, input.provider)
  provider = Provider()  # type: ignore
  load_class(BaseGenerator, input.generator)

  n = len(list(input.function_configs.values())[0])
  for function_configs in input.function_configs.values():
    assert len(
        function_configs
    ) == n, "All functions must have same number of configurations"

  exps: List[Dict[str, FunctionConfig]] = []
  for i in range(n):
    exps.append({
        function_id: function_configs[i]
        for function_id, function_configs in input.function_configs.items()
    })

  results: List[Tuple[Dict[str, FunctionConfig],
                      WorkflowTuningExecutorOutput]] = []

  description = await provider.describe_workflow(input.workflow_id)

  for exp in exps:
    await initialize(
        WorkflowTuningInitializerInput(
            provider=input.provider,
            workflow_id=input.workflow_id,
            description=description,
            function_configs=exp
        )
    )
    results.append((
        exp, await execute(
            WorkflowTuningExecutorInput(
                provider=input.provider,
                workflow_id=input.workflow_id,
                description=description,
                generator=input.generator,
                generator_input=input.generator_input,
                invocation_mode=input.invocation_mode
            )
        )
    ))
  return WorkflowTuningDispatcherOutput(
      description=description, results=results
  )


class WorkflowTuningAnalyserInput(NamedTuple):
  provider: str
  workflow_id: str
  function_configs: Dict[str, List[FunctionConfig]]
  dispatcher_output: WorkflowTuningDispatcherOutput
  algorithm: str
  algorithm_input: Dict[str, Any]


class WorkflowTuningAnalyserOutput(NamedTuple):
  best_config: Dict[str, FunctionConfig]


async def analyze(
    input: WorkflowTuningAnalyserInput
) -> WorkflowTuningAnalyserOutput:
  Provider = load_class(BaseProvider, input.provider)
  provider = Provider()  # type: ignore
  Algorithm = load_class(BaseAlgorithm, input.algorithm)
  algorithm = Algorithm()  # type: ignore
  description = input.dispatcher_output.description
  results = [(configs, result.results)
             for configs, result in input.dispatcher_output.results]
  best_config = algorithm.optimize_workflow(
      input=input.algorithm_input,
      provider=provider,
      workflow_id=input.workflow_id,
      description=description,
      dispatched_results=results
  )
  return WorkflowTuningAnalyserOutput(best_config=best_config)
