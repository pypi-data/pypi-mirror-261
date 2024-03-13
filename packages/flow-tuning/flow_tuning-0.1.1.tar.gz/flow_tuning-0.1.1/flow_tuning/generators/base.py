from abc import ABC
from abc import abstractmethod
from typing import Any, AsyncIterable, Dict, List


class BaseGenerator(ABC):

  @abstractmethod
  def generate_batch(self, input: Dict[str, Any]) -> AsyncIterable[List[Any]]:
    pass
