import dataclasses
import sys

_py310 = sys.version_info.minor >= 10 or sys.version_info.major > 3


def dataclass(*args, **kwargs):
    if not _py310:
        kwargs.pop("slots", None)

    return dataclasses.dataclass(*args, **kwargs)


field = dataclasses.field
asdict = dataclasses.asdict
