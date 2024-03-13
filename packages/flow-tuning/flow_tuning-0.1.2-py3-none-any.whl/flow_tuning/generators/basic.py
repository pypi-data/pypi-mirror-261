from typing import Any, AsyncIterable, List, Literal, override

from flow_tuning.generators.base import BaseGenerator


class BasicGeneratorInput:

  def __init__(
      self,
      total: int,
      payloads: List[Any],
      mode: Literal['serial', 'parallel'] = 'serial'
  ):
    self.total = total
    self.payloads = payloads
    self.mode = mode


class BasicGenerator(BaseGenerator):

  @override
  async def generate_batch(self, input) -> AsyncIterable[List[Any]]:
    input_data = BasicGeneratorInput(**input)
    if input_data.mode == 'serial':
      for i in range(input_data.total):
        yield [input_data.payloads[i % len(input_data.payloads)]]
    else:
      yield [
          input_data.payloads[i % len(input_data.payloads)]
          for i in range(input_data.total)
      ]
