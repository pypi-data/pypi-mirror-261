import enum
from typing import Literal, TypeAlias


class _MISSING(enum.Enum):
    MISSING = enum.auto()


MISSING_T: TypeAlias = Literal[_MISSING.MISSING]
MISSING: MISSING_T = _MISSING.MISSING
