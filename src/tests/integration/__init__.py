from types import ModuleType as __ModuleType
from . import test_basic_render

ALL: tuple[__ModuleType, ...] = (test_basic_render,)
