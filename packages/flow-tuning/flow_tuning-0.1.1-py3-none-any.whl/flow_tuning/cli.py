import asyncio
from dataclasses import dataclass
import pickle
from typing import Annotated, Any, Dict, List, Literal, Optional

import typer
from yaml import load

from flow_tuning.utils.module_loader import load_class

try:
  from yaml import CLoader as Loader
except ImportError:
  from yaml import Loader

import flow_tuning.function as ft_func
from flow_tuning.providers.base import FunctionConfig
from flow_tuning.utils.console import console
import flow_tuning.workflow as ft_flow

app = typer.Typer(pretty_exceptions_show_locals=False)


@dataclass
class FunctionTuningConfig:
  provider: str
  function_id: str
  configs: List[FunctionConfig]
  generator: str
  generator_input: Dict[str, Any]
  invocation_mode: Literal['serial', 'parallel']
  execution_mode: Literal['serial', 'parallel']
  algorithm: str
  algorithm_input: Dict[str, Any]


@app.command()
def function(
    config_path: Annotated[str, typer.Option("--config", "-c")],
    dump_dispatch_to: Annotated[
        Optional[str], typer.Option("--dump-dispatch-to", "-d")] = None,
    load_dispatch_from: Annotated[
        Optional[str],
        typer.Option("--load-dispatch-from", "-l")] = None
):
  with open(config_path, 'r') as f:
    config_data = load(f, Loader)
  config_data['configs'] = [
      FunctionConfig(**config) for config in config_data['configs']
  ]
  config = FunctionTuningConfig(**config_data)

  # Ensure classes can be loaded
  console.log(
      "Using provider=", load_class(ft_func.BaseProvider, config.provider)
  )
  console.log(
      "Using generator=", load_class(ft_func.BaseGenerator, config.generator)
  )
  console.log(
      "Using algorithm=", load_class(ft_func.BaseAlgorithm, config.algorithm)
  )

  function_configs: Dict[str, FunctionConfig] = {}
  for i, function_config in enumerate(config.configs):
    function_configs[f'config-{i}'] = function_config

  async def _wrapper():
    if load_dispatch_from:
      with open(load_dispatch_from, 'rb') as f:
        dispatcher_output = pickle.load(f)
      assert isinstance(
          dispatcher_output, ft_func.FunctionTuningDispatcherOutput
      ), f"Expected FunctionTuningDispatcherOutput, got {type(dispatcher_output)}"
    else:
      initializer_output = await ft_func.initialize(
          ft_func.FunctionTuningInitializerInput(
              provider=config.provider,
              function_id=config.function_id,
              configs=function_configs
          )
      )
      console.log("Function qualifiers generated", initializer_output)

      dispatcher_output = await ft_func.dispatch(
          ft_func.FunctionTuningDispatcherInput(
              provider=config.provider,
              function_id=config.function_id,
              configs=function_configs,
              configured_qualifiers=initializer_output.configured_qualifiers,
              generator=config.generator,
              generator_input=config.generator_input,
              invocation_mode=config.invocation_mode,
              execution_mode=config.execution_mode,
          )
      )
      console.log("Function dispatched")

      await ft_func.clean(
          ft_func.FunctionTuningCleanerInput(
              provider=config.provider,
              function_id=config.function_id,
              configured_qualifiers=initializer_output.configured_qualifiers
          )
      )
      console.log("Function qualifiers cleaned")

      if dump_dispatch_to:
        with open(dump_dispatch_to, 'wb') as f:
          pickle.dump(dispatcher_output, f)
        console.log(f"Dispatch output dumped to {dump_dispatch_to}")

    analyser_output = await ft_func.analyse(
        ft_func.FunctionTuningAnalyserInput(
            provider=config.provider,
            function_id=config.function_id,
            configs=function_configs,
            configured_qualifiers=initializer_output.configured_qualifiers,
            dispatcher_output=dispatcher_output,
            algorithm=config.algorithm,
            algorithm_input=config.algorithm_input
        )
    )
    console.log("Function analysis completed")
    console.log(analyser_output)

  asyncio.run(_wrapper())


@dataclass
class WorkflowTuningConfig:
  provider: str
  workflow_id: str
  function_configs: Dict[str, List[FunctionConfig]]
  generator: str
  generator_input: Dict[str, Any]
  invocation_mode: Literal['serial', 'parallel']
  algorithm: str
  algorithm_input: Dict[str, Any]


@app.command()
def workflow(
    config_path: Annotated[str, typer.Option("--config", "-c")],
    dump_dispatch_to: Annotated[
        Optional[str], typer.Option("--dump-dispatch-to", "-d")] = None,
    load_dispatch_from: Annotated[
        Optional[str],
        typer.Option("--load-dispatch-from", "-l")] = None
):
  with open(config_path, 'r') as f:
    config_data = load(f, Loader)
  config_data["function_configs"] = {
      k: [FunctionConfig(**c) for c in v]
      for k, v in config_data["function_configs"].items()
  }
  config = WorkflowTuningConfig(**config_data)

  console.log(
      "Using provider=", load_class(ft_flow.BaseProvider, config.provider)
  )
  console.log(
      "Using generator=", load_class(ft_flow.BaseGenerator, config.generator)
  )
  console.log(
      "Using algorithm=", load_class(ft_flow.BaseAlgorithm, config.algorithm)
  )

  async def _wrapper():
    if load_dispatch_from:
      with open(load_dispatch_from, 'rb') as f:
        dispatcher_output = pickle.load(f)
      assert isinstance(
          dispatcher_output, ft_flow.WorkflowTuningDispatcherOutput
      ), f"Expected WorkflowTuningDispatcherOutput, got {type(dispatcher_output)}"
    else:
      dispatcher_output = await ft_flow.dispatch(
          ft_flow.WorkflowTuningDispatcherInput(
              provider=config.provider,
              workflow_id=config.workflow_id,
              function_configs=config.function_configs,
              generator=config.generator,
              generator_input=config.generator_input,
              invocation_mode=config.invocation_mode
          )
      )
      console.log("Workflow dispatched")
      if dump_dispatch_to:
        with open(dump_dispatch_to, 'wb') as f:
          pickle.dump(dispatcher_output, f)
        console.log(f"Dispatch output dumped to {dump_dispatch_to}")

    analyser_output = await ft_flow.analyze(
        ft_flow.WorkflowTuningAnalyserInput(
            provider=config.provider,
            workflow_id=config.workflow_id,
            function_configs=config.function_configs,
            dispatcher_output=dispatcher_output,
            algorithm=config.algorithm,
            algorithm_input=config.algorithm_input
        )
    )
    console.log(analyser_output)

    typer.confirm("Apply best configuration?", abort=True)
    await ft_flow.initialize(
        ft_flow.WorkflowTuningInitializerInput(
            provider=config.provider,
            workflow_id=config.workflow_id,
            description=dispatcher_output.description,
            function_configs=analyser_output.best_config
        )
    )
    console.log("Best configuration applied")

  asyncio.run(_wrapper())


if __name__ == "__main__":
  app()
