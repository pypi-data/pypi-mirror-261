from __future__ import annotations

from ._dataclass_fix import dataclass, asdict


@dataclass
class BaseSdp:
    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)

    def clone(self):
        return self.__class__.from_dict(self.to_dict())
