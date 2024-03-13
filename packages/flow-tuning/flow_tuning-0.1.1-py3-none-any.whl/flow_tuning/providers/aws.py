import asyncio
import base64
from dataclasses import dataclass
import json
from math import ceil
import multiprocessing
from multiprocessing import synchronize
import os
import secrets
from time import sleep
from typing import Any, Dict, List, Literal, NamedTuple, Optional, override, Set, Tuple  # NOQA

import boto3
from botocore.exceptions import ClientError

from flow_tuning.providers.base import BaseProvider
from flow_tuning.providers.base import FunctionConfig
from flow_tuning.providers.base import FunctionInvocationResult
from flow_tuning.providers.base import WorkflowDescription
from flow_tuning.providers.base import WorkflowInvocationResult
from flow_tuning.providers.base import WorkflowStepDescription
from flow_tuning.providers.base import WorkflowStepInvocationResult
from flow_tuning.utils.console import console

HistoryEvent = Dict[str, Any]


@dataclass
class AwsWorkflowStepDescription(WorkflowStepDescription):
  log_type: Literal['inline', 'cloudwatch'] = 'cloudwatch'


class EventGraph:
  next: Dict[int, List[int]]
  events: Dict[int, HistoryEvent]
  lambda_stats: Dict[str, "ParsedReportLine"]

  def __init__(
      self, events: List[HistoryEvent], lambda_stats: Dict[str,
                                                           "ParsedReportLine"]
  ):
    self.next = {}
    self.events = {}
    self.lambda_stats = lambda_stats
    for event in events:
      self.events[event['id']] = event
      self.next[event['previousEventId']] \
        = self.next.get(event['previousEventId'], []) + [event['id']]

  def get_next_events(self, event_id: int) -> List[HistoryEvent]:
    return [self.events[event_id] for event_id in self.next.get(event_id, [])]

  def get_exact_next_event(self, event_id: int) -> HistoryEvent:
    next = self.get_next_events(event_id)
    if len(next) != 1:
      raise ValueError(
          f"Expected exactly one next event for {event_id}, got {len(next)}"
      )
    return next[0]

  def get_optional_next_event(self, event_id: int) -> Optional[HistoryEvent]:
    next = self.get_next_events(event_id)
    if len(next) > 1:
      raise ValueError(
          f"Expected at most one next event for {event_id}, got {len(next)}"
      )
    return next[0] if next else None


@dataclass
class AwsFunctionInvocationResult(FunctionInvocationResult):
  raw_log: str
  memory_size: int
  max_memory_used: float
  billed_duration: float


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


def gather_log_groups(
    logGroupIdentifiers: List[str], stop_sig: synchronize.Event,
    result_queue: multiprocessing.Queue
):
  client = boto3.client('logs')
  requests: Dict[str, ParsedReportLine] = {}
  try:
    response = client.start_live_tail(logGroupIdentifiers=logGroupIdentifiers)
    event_stream = response['responseStream']
    for event in event_stream:
      if stop_sig.is_set():
        event_stream.close()
        break

      if 'sessionStart' in event:
        session_start_event = event['sessionStart']
        console.log(f"Started log tail session", session_start_event)

      elif 'sessionUpdate' in event:
        log_events = event['sessionUpdate']['sessionResults']
        for log_event in log_events:
          message: str = log_event['message']
          # REPORT RequestId: 07c3c4ef-ce6f-4a3e-85c7-e36d31c233db ...
          if message.startswith("REPORT RequestId:"):
            request_id = message.split(' ')[2].split('\t')[0]
            requests[request_id] = parse_report_line(message)
            console.log(
                f"Got report for request {request_id}", requests[request_id]
            )
      else:
        # On-stream exceptions are captured here
        raise RuntimeError(str(event))
    result_queue.put(requests)
  except Exception as e:
    console.log(e)
    raise e


class AwsProvider(BaseProvider):

  @classmethod
  def _asl_to_workflow_description(
      cls, asl: Dict[str, Any], prefix: str = '$$'
  ) -> WorkflowDescription:
    start_at = asl.get('StartAt', '')
    states = asl.get('States', {})
    steps: List[WorkflowStepDescription] = []

    for state_name, state_info in states.items():
      # step_id = f"{prefix}.{state_name}"
      step_id = state_name
      step_type = state_info.get('Type').lower()

      if step_type == 'task':
        resource = state_info.get('Resource', '')
        function_id: Optional[str] = None
        if resource in (
            "arn:aws:states:::aws-sdk:lambda:invoke",
            "arn:aws:states:::lambda:invoke"
        ):
          function_id = state_info.get('Parameters', {}).get('FunctionName')
        if function_id and not function_id.endswith(":FT-LATEST"):
          function_id = None
        if function_id:
          function_id = function_id.split(':FT-LATEST')[0]
          log_type = 'cloudwatch' if resource == 'arn:aws:states:::lambda:invoke' else 'inline'
          steps.append(
              AwsWorkflowStepDescription(
                  step_id=step_id,
                  type='function',
                  function_id=function_id,
                  log_type=log_type
              )
          )
        else:
          steps.append(WorkflowStepDescription(step_id=step_id, type='fixed'))

      elif step_type == 'parallel':
        branches = {}
        for i, branch in enumerate(state_info.get('Branches', [])):
          branch_id = f"{step_id}.branch-{i}"
          branch_description = cls._asl_to_workflow_description(
              branch, prefix=branch_id
          )
          branches[branch_description.workflow_id] = branch_description
        steps.append(
            WorkflowStepDescription(
                step_id=step_id, type='parallel', branches=branches
            )
        )

      elif step_type == 'map':
        iterator = state_info.get('ItemProcessor', state_info.get('Iterator'))
        workflow = cls._asl_to_workflow_description(
            iterator, prefix=f"{step_id}.workflow"
        )
        steps.append(
            WorkflowStepDescription(
                step_id=step_id, type='map', workflow=workflow
            )
        )

      # Add more cases as needed for 'Choice', 'Wait', etc.

    return WorkflowDescription(workflow_id=start_at, steps=steps)

  @classmethod
  def _start_gather_log_groups(cls, logGroupIdentifiers: List[str]):
    stop_sig = multiprocessing.Event()
    result_queue = multiprocessing.Queue()
    p = multiprocessing.Process(
        target=gather_log_groups,
        args=(logGroupIdentifiers, stop_sig, result_queue)
    )
    p.start()

    def get_result() -> Dict[str, ParsedReportLine]:
      stop_sig.set()
      p.join()
      return result_queue.get()

    return get_result

  @classmethod
  def _get_cloudwatch_function_ids(
      cls, description: WorkflowDescription
  ) -> Set[str]:
    function_ids = set()
    for step in description.steps:
      if step.type == 'function':
        if isinstance(step, AwsWorkflowStepDescription):
          if step.log_type == 'cloudwatch':
            function_ids.add(step.function_id)
        else:
          raise ValueError('Invalid step type')
      elif step.type in ('parallel', 'branch') and step.branches:
        for branch in step.branches.values():
          function_ids.update(cls._get_cloudwatch_function_ids(branch))
      elif step.type == 'map' and step.workflow:
        function_ids.update(cls._get_cloudwatch_function_ids(step.workflow))
      elif step.type == 'fixed':
        pass
      else:
        raise ValueError(f"Invalid step type: {step.type}")
    return function_ids

  def __init__(self):
    self.lambda_client = boto3.client('lambda')
    self.sfn_client = boto3.client('stepfunctions')
    self.verbose_log_file = os.environ.get('FT_VERBOSE_LOG_FILE', '')
    if self.verbose_log_file:

      def verbose_log(msg: str):
        with open(self.verbose_log_file, 'a') as f:
          f.write(msg + '\n')

      self._verbose_log = verbose_log
    else:
      self._verbose_log = lambda msg: None

  def _get_lambda_base_cost(self, region: str, architecture: str):
    data = {
        'x86_64': {
            'ap-east-1': 2.9e-9,
            'af-south-1': 2.8e-9,
            'me-south-1': 2.6e-9,
            'eu-south-1': 2.4e-9,
            'ap-northeast-3': 2.7e-9,
            'cn-north-1': 0.0000000142,
            'cn-northwest-1': 0.0000000142,
            'default': 2.1e-9
        },
        'arm64': {
            'default': 1.7e-9
        }
    }
    data = data.get(architecture, data['x86_64'])
    data = data.get(region, data['default'])
    return data

  def _get_lambda_cost(self, base_cost: float, duration: float, memory: float):
    # See AWS Lambda Power Tuning source code for the formula
    return base_cost * ceil(duration) * memory / 128

  def _parse_lambda_function_arn(self, arn: str) -> Dict[str, str]:
    parts = arn.split(':')
    if len(parts) < 7 or len(parts) > 8:
      raise ValueError(f'Invalid lambda function ARN: {arn}')
    _, _, _, region, account_id, _, function_name, *qualifier = parts
    return {
        'region': region,
        'account_id': account_id,
        'function_name': function_name,
        'qualifier': qualifier[0] if qualifier else ''
    }

  def _arn_to_region(self, arn: str) -> str:
    return self._parse_lambda_function_arn(arn)['region']

  @override
  def get_function_cost(self, function_id, config, duration):
    region = self._arn_to_region(function_id)
    architecture = 'x86_64'
    base_cost = self._get_lambda_base_cost(region, architecture)
    billed_duration = ceil(duration)
    return self._get_lambda_cost(base_cost, billed_duration, config.memory)

  @override
  async def configure_function(
      self, function_id: str, qualifier: str, config: FunctionConfig
  ) -> None:
    try:
      # Update function configuration
      self.lambda_client.update_function_configuration(
          FunctionName=function_id, MemorySize=config.memory
      )
      console.log(f"Updated function {function_id} to memory {config.memory}")

      waiter = self.lambda_client.get_waiter('function_updated')
      waiter.wait(FunctionName=function_id)

      # Publish a new version
      response = self.lambda_client.publish_version(FunctionName=function_id)
      version = response['Version']
      console.log(f"Published version {version} for function {function_id}")

      # Update or create alias
      try:
        self.lambda_client.update_alias(
            FunctionName=function_id, Name=qualifier, FunctionVersion=version
        )
      except self.lambda_client.exceptions.ResourceNotFoundException:
        self.lambda_client.create_alias(
            FunctionName=function_id, Name=qualifier, FunctionVersion=version
        )

      waiter = self.lambda_client.get_waiter('function_updated')
      waiter.wait(FunctionName=function_id, Qualifier=qualifier)

      console.log(
          f"Configured alias {qualifier} for version {version} of function {function_id}"
      )
    except ClientError as error:
      console.log(f"Error configuring function: {error}")

  @override
  async def deconfigure_function(
      self, function_id: str, qualifier: str
  ) -> None:
    try:
      # Delete the specified alias and its associated version
      alias_info = self.lambda_client.get_alias(
          FunctionName=function_id, Name=qualifier
      )
      function_version = alias_info['FunctionVersion']

      self.lambda_client.delete_alias(FunctionName=function_id, Name=qualifier)
      console.log(f"Deleted alias {qualifier} for function {function_id}")

      self.lambda_client.delete_function(
          FunctionName=function_id, Qualifier=function_version
      )
      console.log(
          f"Deleted version {function_version} of function {function_id}"
      )
    except ClientError as error:
      console.log(f"Error deconfiguring function: {error}")

  @override
  async def invoke_function(
      self, function_id: str, qualifier: str, payload: Any
  ) -> AwsFunctionInvocationResult:
    try:
      response = self.lambda_client.invoke(
          FunctionName=function_id,
          Qualifier=qualifier,
          Payload=json.dumps(payload),
          LogType='Tail'
      )
      log_result = base64.b64decode(response['LogResult']).decode('utf-8')
      self._verbose_log(
          f"=== LOG RESULT FOR {function_id}:{qualifier} ===\n"
          f"{log_result}"
      )
      log_lines = log_result.split('\n')
      report_line = next(
          (line for line in log_lines if line.startswith('REPORT RequestId:')),
          None
      )
      if not report_line:
        raise ValueError('Report line not found')

      parsed = parse_report_line(report_line)

      # Construct and return a FunctionInvocationResult object
      return AwsFunctionInvocationResult(
          output=response.get('Payload', {}
                             ).read().decode('utf-8'),  # Assuming JSON response
          task_duration=parsed.duration,
          billed_duration=parsed.billed_duration,
          raw_log=log_result,
          memory_size=parsed.memory_size,
          max_memory_used=parsed.max_memory_used,
          init_duration=parsed.init_duration
      )
    except ClientError as error:
      console.log(f"Error invoking function: {error}")
      raise error

  @override
  async def describe_workflow(self, workflow_id: str) -> WorkflowDescription:
    try:
      response = self.sfn_client.describe_state_machine(
          stateMachineArn=workflow_id
      )
      asl = json.loads(response['definition'])
      return self._asl_to_workflow_description(asl)
    except ClientError as error:
      console.log(f"Error describing workflow: {error}")
      raise error

  async def _get_lambda_log_group_arn(self, function_arn: str) -> str:
    function = self.lambda_client.get_function(FunctionName=function_arn)
    group = function["Configuration"]["LoggingConfig"]["LogGroup"]
    function_parts = self._parse_lambda_function_arn(function_arn)
    return f"arn:aws:logs:{function_parts['region']}:{function_parts['account_id']}:log-group:{group}"

  async def _get_execution_full_events(
      self, execution_arn: str
  ) -> List[HistoryEvent]:
    response = self.sfn_client.get_execution_history(executionArn=execution_arn)
    events = response['events']
    next_token = response.get('nextToken')
    while next_token:
      response = self.sfn_client.get_execution_history(
          executionArn=execution_arn, nextToken=next_token
      )
      events.extend(response['events'])
      next_token = response.get('nextToken')
    console.log(f"Got {len(events)} events for execution {execution_arn}")
    return events

  async def _parse_task_state_events(
      self, g: EventGraph, entry: int
  ) -> Tuple[WorkflowStepInvocationResult, int]:
    ev = g.events[entry]
    name = ev.get('stateEnteredEventDetails', {}).get('name')
    if not name:
      raise ValueError('Task state name not found')
    while ev.get('type') != 'TaskScheduled':
      ev = g.get_exact_next_event(ev['id'])
    parameters = json.loads(ev['taskScheduledEventDetails']['parameters'])
    function_arn = parameters['FunctionName']
    while ev.get('type') != 'TaskStarted':
      ev = g.get_exact_next_event(ev['id'])
    start_ts = ev.get('timestamp')
    if not start_ts:
      raise ValueError('Task start timestamp not found')

    while ev.get('type') != 'TaskSucceeded':
      ev = g.get_exact_next_event(ev['id'])
    end_ts = ev.get('timestamp')
    if not end_ts:
      raise ValueError('Task end timestamp not found')

    duration = (end_ts - start_ts).total_seconds() * 1000
    task_duration = duration
    billed_duration = duration
    init_duration = 0
    cost = 0
    resource_type = ev['taskSucceededEventDetails']['resourceType']
    match resource_type:
      case 'aws-sdk:lambda':
        output = json.loads(ev['taskSucceededEventDetails']['output'])
        log_result = base64.b64decode(output['LogResult']).decode('utf-8')
        log_lines = log_result.split('\n')
        report_line = next(
            filter(
                lambda line: line.startswith('REPORT RequestId:'), log_lines
            ), None
        )
        if not report_line:
          raise ValueError('Report line not found')
        parsed = parse_report_line(report_line)
      case 'lambda':
        # x-amzn-RequestId
        output = json.loads(ev['taskSucceededEventDetails']['output'])
        request_id = output['SdkResponseMetadata']['RequestId']
        parsed = g.lambda_stats[request_id]
    if parsed:
      console.log(f"Parsed result for {function_arn}", parsed)
      task_duration = parsed.duration
      billed_duration = parsed.billed_duration
      init_duration = parsed.init_duration
      cost = self._get_lambda_cost(
          self._get_lambda_base_cost(
              self._arn_to_region(function_arn), 'x86_64'
          ), parsed.duration, parsed.memory_size
      )

    while ev.get('type') != 'TaskStateExited':
      ev = g.get_exact_next_event(ev['id'])

    return WorkflowStepInvocationResult(
        step_id=name,
        duration=duration,
        task_duration=task_duration,
        init_duration=init_duration,
    ), ev['id']

  async def _parse_parallel_state_events(
      self, g: EventGraph, entry: int
  ) -> Tuple[WorkflowStepInvocationResult, int]:
    ev = g.events[entry]
    name = ev.get('stateEnteredEventDetails', {}).get('name')
    if not name:
      raise ValueError('Parallel state name not found')
    while ev.get('type') != 'ParallelStateStarted':
      ev = g.get_exact_next_event(ev['id'])
    start_ts = ev.get('timestamp')
    if not start_ts:
      raise ValueError('Parallel state start timestamp not found')

    results = g.get_next_events(ev['id'])
    results = [
        self._parse_workflow_events(g, e['id'], 'ParallelStateExited')
        for e in results
    ]
    results = await asyncio.gather(*results)
    nexts = [g.events[r[1]] for r in results if r[1] != -1]
    if len(nexts) != 1:
      raise ValueError(
          f"Expected exactly one ParallelStateExited event, got {len(nexts)}"
      )
    ev = nexts[0]
    end_ts = ev.get('timestamp')
    if not end_ts:
      raise ValueError('Parallel state end timestamp not found')
    duration = (end_ts - start_ts).total_seconds() * 1000
    return WorkflowStepInvocationResult(
        step_id=name,
        duration=duration,
        task_duration=duration,
        init_duration=0,
        branched_results={p[0].steps[0].step_id: p[0] for p in results}
    ), ev['id']

  async def _parse_map_state_events(
      self, g: EventGraph, entry: int
  ) -> Tuple[WorkflowStepInvocationResult, int]:
    ev = g.events[entry]
    name = ev.get('stateEnteredEventDetails', {}).get('name')
    if not name:
      raise ValueError('Map state name not found')
    while ev.get('type') != 'MapStateStarted':
      ev = g.get_exact_next_event(ev['id'])
    start_ts = ev.get('timestamp')
    if not start_ts:
      raise ValueError('Map state start timestamp not found')

    results = g.get_next_events(ev['id'])
    results = [
        self._parse_workflow_events(
            g=g,
            entry=g.get_exact_next_event(e['id'])['id'],
            expectedEnd='MapIterationSucceeded'
        ) for e in results
    ]
    results = await asyncio.gather(*results)
    nexts = [
        ev for r in results if r[1] != -1 for ev in g.get_next_events(r[1])
        if ev['type'] == 'MapStateExited'
    ]
    if len(nexts) != 1:
      raise ValueError(
          f"Expected exactly one MapStateExited event, got {len(nexts)}"
      )
    ev = nexts[0]
    end_ts = ev.get('timestamp')
    if not end_ts:
      raise ValueError('Map state end timestamp not found')
    duration = (end_ts - start_ts).total_seconds() * 1000
    return WorkflowStepInvocationResult(
        step_id=name,
        duration=duration,
        task_duration=duration,
        init_duration=0,
        mapped_results=[p[0] for p in results]
    ), ev['id']

  async def _parse_workflow_events(
      self, g: EventGraph, entry: int, expectedEnd: str
  ) -> Tuple[WorkflowInvocationResult, int]:
    result = WorkflowInvocationResult('', [])
    while entry != -1:
      ev = g.events[entry]
      step: Tuple[WorkflowStepInvocationResult, int]
      match ev['type']:
        case 'TaskStateEntered':
          step = await self._parse_task_state_events(g, entry)
        case 'ParallelStateEntered':
          step = await self._parse_parallel_state_events(g, entry)
        case 'MapStateEntered':
          step = await self._parse_map_state_events(g, entry)
        case _:
          raise ValueError(f"Unexpected event type: {ev['type']}")
      if not result.workflow_id:
        result.workflow_id = step[0].step_id
      result.steps.append(step[0])
      nx = g.get_next_events(step[1])
      matched = next(filter(lambda e: e['type'] == expectedEnd, nx), None)
      if matched:
        return result, matched['id']
      # find events with stateEnteredEventDetails attr
      entered = list(filter(lambda e: 'stateEnteredEventDetails' in e, nx))
      if not entered:
        break
      if len(entered) > 1:
        raise ValueError(
            f"Expected at most one stateEnteredEventDetails event, got {len(entered)}"
        )
      entry = entered[0]['id']
    return result, -1

  async def _parse_workflow_execution_events(
      self, lambda_stats: Dict[str, ParsedReportLine],
      events: List[HistoryEvent]
  ):
    graph = EventGraph(events, lambda_stats)
    initList = graph.get_next_events(0)
    if len(initList) != 2:
      raise ValueError(
          f"Expected exactly 2 initial events, got {len(initList)}"
      )
    init = next(
        filter(lambda e: e['type'] != 'ExecutionStarted', initList), None
    )
    if not init:
      raise ValueError("No initial event found")
    result, _ = await self._parse_workflow_events(
        graph, init['id'], 'ExecutionSucceeded'
    )
    return result

  async def _load_results_from_execution(
      self, lambda_stats: Dict[str, ParsedReportLine], execution_arn: str
  ):
    events = await self._get_execution_full_events(execution_arn)
    return await self._parse_workflow_execution_events(lambda_stats, events)

  @override
  async def invoke_workflow(
      self, workflow_id: str, description: WorkflowDescription, payload: Any
  ) -> WorkflowInvocationResult:
    function_ids = self._get_cloudwatch_function_ids(description)
    log_group_arns = [
        await self._get_lambda_log_group_arn(function_id)
        for function_id in function_ids
    ]
    if not log_group_arns:
      console.log("No need to gather logs")
      get_lambda_stats = lambda: {}
    else:
      stop = self._start_gather_log_groups(log_group_arns)
      get_lambda_stats = lambda: sleep(30) or stop()
    sleep(5)
    response = self.sfn_client.start_execution(
        stateMachineArn=workflow_id,
        name=f"FT-{secrets.token_hex(16)}",
        input=json.dumps(payload)
    )
    execution_arn = response['executionArn']
    console.log(f"Started execution {execution_arn} of workflow {workflow_id}")
    while True:
      response = self.sfn_client.describe_execution(executionArn=execution_arn)
      status = response['status']
      if status in ('SUCCEEDED', 'FAILED', 'TIMED_OUT', 'ABORTED'):
        if status == 'SUCCEEDED':
          break
        else:
          raise ValueError(
              f"Workflow execution {execution_arn} failed with status {status}"
          )
      await asyncio.sleep(1)
    console.log(
        f"Execution {execution_arn} of workflow {workflow_id} completed"
    )
    lambda_stats = get_lambda_stats()
    console.log(lambda_stats)
    return await self._load_results_from_execution(lambda_stats, execution_arn)
