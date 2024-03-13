import asyncio
import base64
from dataclasses import dataclass
from datetime import datetime
import json
from math import ceil
from math import floor
import os
import secrets
from typing import Any, Dict, List, Literal, NamedTuple, Optional, override, Tuple, TypeVar  # NOQA

from alibabacloud_fc_open20210406 import models as fc_models
from alibabacloud_fc_open20210406.client import Client as FcClient
from alibabacloud_fnf20190315 import models as fnf_models
from alibabacloud_fnf20190315.client import Client as FnfClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util import models as util_models
from Tea.exceptions import TeaException
from yaml import load

from flow_tuning.providers.base import BaseProvider
from flow_tuning.providers.base import FunctionConfig
from flow_tuning.providers.base import FunctionInvocationResult
from flow_tuning.providers.base import WorkflowDescription
from flow_tuning.providers.base import WorkflowInvocationResult
from flow_tuning.providers.base import WorkflowStepDescription
from flow_tuning.providers.base import WorkflowStepInvocationResult
from flow_tuning.utils.console import console

try:
  from yaml import CLoader as Loader
except ImportError:
  from yaml import Loader

T = TypeVar('T')


def must(x: Optional[T]) -> T:
  assert x is not None, f"Expected not None, got {x}"
  return x


@dataclass
class AliyunFunctionInvocationResult(FunctionInvocationResult):
  max_memory_used: float


class ParsedReportLine(NamedTuple):
  duration: float
  billed_duration: float
  memory_size: int
  max_memory_used: float
  init_duration: float


def parse_report_line(line: str):

  def parse_field(key: str, unit: str) -> Optional[str]:
    parts = line.split(f'{key}: ')
    if len(parts) < 2:
      return None
    return parts[1].split(f' {unit}')[0].strip()

  return ParsedReportLine(
      duration=float(parse_field('Duration', 'ms') or '0'),
      billed_duration=float(parse_field('Billed Duration', 'ms') or '0'),
      memory_size=int(parse_field('Memory Size', 'MB') or '0'),
      max_memory_used=float(parse_field('Max Memory Used', 'MB') or '0'),
      init_duration=float(parse_field('Init Duration', 'ms') or '0'),
  )


class EventGraph:
  next: Dict[int, List[int]]
  events: Dict[int, fnf_models.GetExecutionHistoryResponseBodyEvents]

  def __init__(
      self,
      events: List[fnf_models.GetExecutionHistoryResponseBodyEvents],
  ):
    self.next = {}
    self.events = {}
    for event in events:
      if not event.event_id:
        raise ValueError(f"Event {event} do not have event_id")
      self.events[event.event_id] = event
      if event.schedule_event_id == None:
        raise ValueError(f"Event {event} do not have schedule_event_id")
      self.next[event.schedule_event_id] \
        = self.next.get(event.schedule_event_id, []) + [event.event_id]

  def get_next_events(
      self, event_id: int
  ) -> List[fnf_models.GetExecutionHistoryResponseBodyEvents]:
    return [self.events[event_id] for event_id in self.next.get(event_id, [])]

  def get_exact_next_event(
      self, event_id: int
  ) -> fnf_models.GetExecutionHistoryResponseBodyEvents:
    next = self.get_next_events(event_id)
    if len(next) != 1:
      raise ValueError(
          f"Expected exactly one next event for {event_id}, got {len(next)}"
      )
    return next[0]

  def get_optional_next_event(
      self, event_id: int
  ) -> Optional[fnf_models.GetExecutionHistoryResponseBodyEvents]:
    next = self.get_next_events(event_id)
    if len(next) > 1:
      raise ValueError(
          f"Expected at most one next event for {event_id}, got {len(next)}"
      )
    return next[0] if next else None


class AliyunProvider(BaseProvider):

  def __init__(self) -> None:
    config = open_api_models.Config(
        access_key_id=os.environ['ALIYUN_ACCESS_KEY_ID'],
        access_key_secret=os.environ['ALIYUN_ACCESS_KEY_SECRET'],
        endpoint=os.environ['FC_ENDPOINT']
    )
    self.fc_client = FcClient(config)

    config = open_api_models.Config(
        access_key_id=os.environ['ALIYUN_ACCESS_KEY_ID'],
        access_key_secret=os.environ['ALIYUN_ACCESS_KEY_SECRET'],
        endpoint=os.environ['FNF_ENDPOINT']
    )
    self.fnf_client = FnfClient(config)

  @override
  async def configure_function(
      self, function_id: str, qualifier: str, config: FunctionConfig
  ) -> None:
    service_name, function_name = function_id.split("$")
    resp = self.fc_client.update_function(
        service_name=service_name,
        function_name=function_name,
        request=fc_models.UpdateFunctionRequest(
            memory_size=int(config.memory),
            cpu=floor(config.memory / 1024 * 20) / 20
        )
    )
    resp = self.fc_client.publish_service_version(
        service_name=service_name,
        request=fc_models.PublishServiceVersionRequest(
            description="Flow Tuning AutoConf"
        )
    )
    version_id = resp.body.version_id
    if not version_id:
      raise ValueError(f"Failed to publish version for {function_id}")
    console.log(f"Published {version_id} for {function_id} with {config}")
    try:
      self.fc_client.update_alias(
          service_name=service_name,
          alias_name=qualifier,
          request=fc_models.UpdateAliasRequest(
              version_id=version_id, description="Flow Tuning AutoConf"
          )
      )
      console.log(
          f"Updated alias {qualifier} for {function_id} to {version_id}"
      )
    except TeaException as e:
      if e.code != 'AliasNotFound':
        raise e

      self.fc_client.create_alias(
          service_name=service_name,
          request=fc_models.CreateAliasRequest(
              alias_name=qualifier,
              version_id=version_id,
              description="Flow Tuning AutoConf"
          )
      )
      console.log(
          f"Created alias {qualifier} for {function_id} to {version_id}"
      )

  @override
  async def deconfigure_function(
      self, function_id: str, qualifier: str
  ) -> None:
    service_name, _ = function_id.split("$")
    resp = self.fc_client.get_alias(
        service_name=service_name, alias_name=qualifier
    )
    if not resp.body.version_id:
      raise ValueError(f"Alias {qualifier} do not contain version")

    self.fc_client.delete_alias(service_name=service_name, alias_name=qualifier)
    self.fc_client.delete_service_version(
        service_name=service_name, version_id=resp.body.version_id
    )

  @override
  async def invoke_function(
      self, function_id: str, qualifier: str, payload: Any
  ) -> FunctionInvocationResult:
    service_name, function_name = function_id.split("$")
    resp = self.fc_client.invoke_function(
        service_name=service_name,
        function_name=function_name,
        request=fc_models.InvokeFunctionRequest(
            qualifier=qualifier, body=json.dumps(payload).encode("utf-8")
        ),
    )
    if not resp.headers:
      raise ValueError(f"Failed to invoke {function_id}")
    duration = float(resp.headers['x-fc-invocation-duration'])
    max_memory_used = float(resp.headers['x-fc-max-memory-usage'])

    return AliyunFunctionInvocationResult(
        output=(resp.body or b'').decode("utf-8"),
        task_duration=duration,
        init_duration=0,
        max_memory_used=max_memory_used,
    )

  @classmethod
  def _fdl_to_workflow_description(
      cls, fdl: Dict[str, Any], prefix: str = '$$'
  ) -> WorkflowDescription:
    start_at = fdl.get('StartAt', '')
    states = fdl.get('States', {})
    steps: List[WorkflowStepDescription] = []

    for state_info in states:
      state_name = state_info['Name']
      # step_id = f"{prefix}.{state_name}"
      step_id = state_name
      step_type = state_info['Type']

      match step_type:
        case 'Pass':
          steps.append(WorkflowStepDescription(step_id=step_id, type='fixed'))

        case 'Task':
          action = state_info['Action']
          function_id: Optional[str] = None
          if action == 'FC:InvokeFunction':
            arn: str = state_info['Parameters']['resourceArn']
            _, service_name, _, function_name = arn.split(':')[-1].split('/')
            service_name, qualifier = service_name.split('.')
            if qualifier == "FT-LATEST":
              function_id = f"{service_name}${function_name}"
          if function_id:
            steps.append(
                WorkflowStepDescription(
                    step_id=step_id, type='function', function_id=function_id
                )
            )
          else:
            steps.append(WorkflowStepDescription(step_id=step_id, type='fixed'))

        case 'Parallel':
          branches = {}
          for i, branch in enumerate(state_info.get('Branches', [])):
            branch_id = f"{step_id}.branch-{i}"
            branch_description = cls._fdl_to_workflow_description(
                branch, prefix=branch_id
            )
            branches[branch_description.workflow_id] = branch_description
          steps.append(
              WorkflowStepDescription(
                  step_id=step_id, type='parallel', branches=branches
              )
          )

        case 'Map':
          iterator = state_info['Processor']
          workflow = cls._fdl_to_workflow_description(
              iterator, prefix=f"{step_id}.workflow"
          )
          steps.append(
              WorkflowStepDescription(
                  step_id=step_id, type='map', workflow=workflow
              )
          )

        case _:
          raise ValueError(f"Unsupported step type: {step_type}")

    return WorkflowDescription(workflow_id=start_at, steps=steps)

  @override
  def get_function_cost(
      self, function_id: str, config: FunctionConfig, duration: float
  ) -> float:
    # https://help.aliyun.com/zh/fc/product-overview/billing-overview#838e9e107ench
    return config.memory * duration * 0.000009

  @override
  async def describe_workflow(self, workflow_id: str) -> WorkflowDescription:
    resp = self.fnf_client.describe_flow(
        fnf_models.DescribeFlowRequest(name=workflow_id)
    )
    if not resp.body.definition:
      raise ValueError(f"Failed to describe workflow {workflow_id}")
    fdl = load(resp.body.definition, Loader)
    assert fdl['Type'] == 'StateMachine', f"Unsupported type: {fdl['Type']}"
    return self._fdl_to_workflow_description(fdl)

  async def _get_execution_full_events(
      self, workflow_name: str, execution_name: str
  ) -> List[fnf_models.GetExecutionHistoryResponseBodyEvents]:
    resp = self.fnf_client.get_execution_history(
        fnf_models.GetExecutionHistoryRequest(
            flow_name=workflow_name, execution_name=execution_name
        )
    )
    events = resp.body.events
    next_token = resp.body.next_token
    while next_token:
      response = self.fnf_client.get_execution_history(
          fnf_models.GetExecutionHistoryRequest(
              flow_name=workflow_name,
              execution_name=execution_name,
              next_token=next_token
          )
      )
      events.extend(response.body.events)
      next_token = response.body.next_token
    console.log(f"Got {len(events)} events for execution {execution_name}")
    return events

  @classmethod
  def _parse_time_str(cls, time_str: str | None):
    assert time_str, f"Expected time_str, got {time_str}"
    time_str = time_str.split('Z')[0]
    parts = time_str.split('.')
    if len(parts) == 1:
      time_str = f"{parts[0]}.000Z"
    else:
      time_str = f"{parts[0]}.{parts[1].ljust(3, '0')}Z"
    ts = datetime.strptime(time_str, '%Y-%m-%dT%H:%M:%S.%fZ')
    return int(ts.timestamp() * 1000)

  async def _parse_step_events(
      self, g: EventGraph, start_id: int, description: WorkflowStepDescription
  ) -> Tuple[WorkflowStepInvocationResult, int]:
    ev = g.events[start_id]
    assert ev.type == "StateEnter", f"Expected StateEnter, got {ev.type}"
    start_time = self._parse_time_str(ev.time)
    match description.type:
      case 'fixed':
        while ev.type != 'StateSucceeded':
          ev = g.get_exact_next_event(must(ev.event_id))
        end_time = self._parse_time_str(ev.time)
        return (
            WorkflowStepInvocationResult(
                step_id=description.step_id,
                duration=end_time - start_time,
                init_duration=0,
                task_duration=end_time - start_time,
            ), must(g.get_exact_next_event(must(ev.event_id)).event_id)
        )

      case 'function':
        while ev.type != 'TaskSucceeded':
          ev = g.get_exact_next_event(must(ev.event_id))
        detail = json.loads(must(ev.event_detail))
        headers = detail['output']['Header']
        duration = float(headers['X-Fc-Invocation-Duration'][0])
        max_memory_used = float(headers['X-Fc-Max-Memory-Usage'][0])
        while ev.type != 'StateSucceeded':
          ev = g.get_exact_next_event(must(ev.event_id))
        end_time = self._parse_time_str(ev.time)
        return (
            WorkflowStepInvocationResult(
                step_id=description.step_id,
                duration=end_time - start_time,
                init_duration=0,
                task_duration=duration,
            ), must(g.get_exact_next_event(must(ev.event_id)).event_id)
        )

      case 'parallel':
        while ev.type != 'StateExec':
          ev = g.get_exact_next_event(must(ev.event_id))
        branches = [(
            must(ev.event_id),
            must(g.get_exact_next_event(must(ev.event_id)).step_name)
        ) for ev in g.get_next_events(must(ev.event_id))]
        branches = await asyncio.gather(
            *[
                self.
                _parse_workflow_events(g, id,
                                       must(description.branches)[name])
                for id, name in branches
            ]
        )
        next_event_id = [id for _, id in branches if id != None]
        assert len(next_event_id) == 1, f"Expected exactly one next event"
        ev = g.events[next_event_id[0]]
        while ev.type != 'StateSucceeded':
          ev = g.get_exact_next_event(must(ev.event_id))
        end_time = self._parse_time_str(ev.time)
        return (
            WorkflowStepInvocationResult(
                step_id=description.step_id,
                duration=end_time - start_time,
                init_duration=0,
                task_duration=end_time - start_time,
                branched_results={
                    result.workflow_id: result for result, _ in branches
                }
            ), must(g.get_exact_next_event(must(ev.event_id)).event_id)
        )

      case 'map':
        while ev.type != 'StateExec':
          ev = g.get_exact_next_event(must(ev.event_id))
        iterations = [
            must(ev.event_id) for ev in g.get_next_events(must(ev.event_id))
        ]
        iterations = await asyncio.gather(
            *[
                self._parse_workflow_events(g, id, must(description.workflow))
                for id in iterations
            ]
        )
        next_event_id = [id for _, id in iterations if id != None]
        assert len(next_event_id) == 1, f"Expected exactly one next event"
        ev = g.events[next_event_id[0]]
        while ev.type != 'StateSucceeded':
          ev = g.get_exact_next_event(must(ev.event_id))
        end_time = self._parse_time_str(ev.time)
        return (
            WorkflowStepInvocationResult(
                step_id=description.step_id,
                duration=end_time - start_time,
                init_duration=0,
                task_duration=end_time - start_time,
                mapped_results=[result for result, _ in iterations]
            ), must(g.get_exact_next_event(must(ev.event_id)).event_id)
        )

      case _:
        raise ValueError(f"Unsupported step type: {description.type}")

  async def _parse_workflow_events(
      self, g: EventGraph, id: int, description: WorkflowDescription
  ) -> Tuple[WorkflowInvocationResult, Optional[int]]:
    ev = g.events[id]
    assert ev.type == "StateEnter", f"Expected StateEnter, got {ev.type}"
    start_event_id = must(g.get_exact_next_event(id).event_id)
    result = WorkflowInvocationResult(
        workflow_id=description.workflow_id, steps=[]
    )
    for step in description.steps:
      step, start_event_id = await self._parse_step_events(
          g, start_event_id, step
      )
      result.steps.append(step)
    ev = g.events[start_event_id]
    assert ev.type == "StateSucceeded", f"Expected StateSucceeded, got {ev.type}"
    ev = g.get_optional_next_event(start_event_id)
    next_event_id = ev.event_id if ev else None
    return result, next_event_id

  async def _parse_workflow_execution_events(
      self, events: List[fnf_models.GetExecutionHistoryResponseBodyEvents],
      description: WorkflowDescription
  ):
    graph = EventGraph(events)
    result, _ = await self._parse_workflow_events(graph, 1, description)
    return result

  async def _load_results_from_execution(
      self, flow_name: str, execution_name: str,
      description: WorkflowDescription
  ) -> WorkflowInvocationResult:
    events = await self._get_execution_full_events(flow_name, execution_name)
    return await self._parse_workflow_execution_events(events, description)

  @override
  async def invoke_workflow(
      self, workflow_id: str, description: WorkflowDescription, payload: Any
  ) -> WorkflowInvocationResult:
    resp = self.fnf_client.start_execution(
        fnf_models.StartExecutionRequest(
            flow_name=workflow_id,
            execution_name=f"FT-{secrets.token_hex(16)}",
            input=json.dumps(payload)
        )
    )
    execution_name = resp.body.name
    if not execution_name:
      raise ValueError(f"Failed to start execution for workflow {workflow_id}")
    console.log(
        f"Started execution {execution_name} for workflow {workflow_id}"
    )
    while True:
      resp = self.fnf_client.describe_execution(
          fnf_models.DescribeExecutionRequest(
              flow_name=workflow_id, execution_name=execution_name
          )
      )
      if resp.body.status in ('Succeeded', 'Failed'):
        break
      console.log(f"Execution {execution_name} status: {resp.body.status}")
      await asyncio.sleep(1)
    if resp.body.status != 'Succeeded':
      raise ValueError(
          f"Execution {execution_name} failed with status {resp.body.status}"
      )
    console.log(f"Execution {execution_name} succeeded")
    await asyncio.sleep(5)
    return await self._load_results_from_execution(
        workflow_id, execution_name, description
    )
