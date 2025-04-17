from types import ModuleType as __ModuleType
from . import (
    test_basic_render,
    test_win_lost,
    test_color,
    test_door,
    test_enemy,
    test_maps,
)

ALL: tuple[__ModuleType, ...] = (
    test_basic_render,
    test_win_lost,
    test_color,
    test_door,
    test_enemy,
    test_maps,
)
