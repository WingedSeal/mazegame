from types import ModuleType as __ModuleType
from . import test_map_creation

ALL: tuple[__ModuleType, ...] = (test_map_creation,)
