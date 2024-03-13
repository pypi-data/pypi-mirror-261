from __future__ import annotations

from ._dataclass_fix import dataclass

from semanticsdp import BaseSdp


@dataclass(slots=True, eq=True)
class DatachannelInfo(BaseSdp):
    port: int
    max_message_size: int
