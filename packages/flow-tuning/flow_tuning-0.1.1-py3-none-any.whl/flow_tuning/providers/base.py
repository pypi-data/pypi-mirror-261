from abc import ABC
from abc import abstractmethod
from dataclasses import dataclass
from typing import Any, Dict, List, Literal, Optional


@dataclass
class FunctionConfig:
  # Memory in MB
  memory: float

  def __eq__(self, other: object) -> bool:
    if not isinstance(other, FunctionConfig):
      return False
    return self.memory == other.memory

  def __hash__(self) -> int:
    return hash(self.memory)


@dataclass
class FunctionInvocationResult:
  output: Any
  """The function output"""

  init_duration: float
  """Init duration"""

  task_duration: float
  """Task duration"""


@dataclass
class WorkflowStepDescription:
  step_id: str
  type: Literal["fixed", "function", "branch", "parallel", "map"]
  function_id: Optional[str] = None
  branches: Optional[Dict[str, "WorkflowDescription"]] = None
  workflow: Optional["WorkflowDescription"] = None


@dataclass
class WorkflowDescription:
  workflow_id: str
  steps: List[WorkflowStepDescription]


@dataclass
class WorkflowStepInvocationResult:
  step_id: str

  duration: float
  """End-to-end duration"""

  init_duration: float
  """Init duration"""

  task_duration: float
  """Task duration"""

  branched_results: Optional[Dict[str, "WorkflowInvocationResult"]] = None
  mapped_results: Optional[List["WorkflowInvocationResult"]] = None


@dataclass
class WorkflowInvocationResult:
  workflow_id: str
  steps: List[WorkflowStepInvocationResult]


class BaseProvider(ABC):

  @abstractmethod
  async def configure_function(
      self, function_id: str, qualifier: str, config: FunctionConfig
  ) -> None:
    pass

  @abstractmethod
  async def deconfigure_function(
      self, function_id: str, qualifier: str
  ) -> None:
    pass

  @abstractmethod
  async def invoke_function(
      self, function_id: str, qualifier: str, payload: Any
  ) -> FunctionInvocationResult:
    pass

  @abstractmethod
  def get_function_cost(
      self, function_id: str, config: FunctionConfig, duration: float
  ) -> float:
    pass

  @abstractmethod
  async def describe_workflow(self, workflow_id: str) -> WorkflowDescription:
    pass

  @abstractmethod
  async def invoke_workflow(
      self, workflow_id: str, description: WorkflowDescription, payload: Any
  ) -> WorkflowInvocationResult:
    pass
