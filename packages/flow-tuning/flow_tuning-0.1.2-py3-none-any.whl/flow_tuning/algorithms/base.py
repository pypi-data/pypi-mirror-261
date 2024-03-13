from abc import ABC
from abc import abstractmethod
from typing import Any, AsyncIterable, Dict, List, Tuple

from flow_tuning.providers.base import BaseProvider
from flow_tuning.providers.base import FunctionConfig
from flow_tuning.providers.base import FunctionInvocationResult
from flow_tuning.providers.base import WorkflowDescription
from flow_tuning.providers.base import WorkflowInvocationResult

FunctionDispatchedResults = List[Tuple[FunctionConfig,
                                       List[FunctionInvocationResult]]]
WorkflowDispatchedResults = List[Tuple[Dict[str, FunctionConfig],
                                       List[WorkflowInvocationResult]]]


class BaseAlgorithm(ABC):

  @abstractmethod
  def optimize_function(
      self, input: Dict[str, Any], provider: BaseProvider, function_id: str,
      dispatched_results: FunctionDispatchedResults
  ) -> FunctionConfig:
    pass

  @abstractmethod
  def optimize_workflow(
      self, input: Dict[str, Any], provider: BaseProvider, workflow_id: str,
      description: WorkflowDescription,
      dispatched_results: WorkflowDispatchedResults
  ) -> Dict[str, FunctionConfig]:
    pass
