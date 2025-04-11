import sys  # noqa

sys.path.append("./src")  # noqa

import os
import unittest
from mazegame import *
from mazegame.color import Color
from mazegame.map import (
    Block,
    ColoredBlock,
    ColoredFloor,
    Door,
    Enemy,
    Exit,
    Key,
    Map,
    Player,
    Spike,
)
from mazegame.api.run import _test_run


def empty_script():
    pass


class TestColors(unittest.TestCase):

    def test_colored_block(self):
        map = Map([[ColoredBlock(color) for color in list(Color)]])
        # _test_run(empty_script, map, exit_on_tick=None, is_render=True)
        _test_run(empty_script, map, exit_on_tick=1)

    def test_colored_floor(self):
        map = Map([[ColoredFloor(color) for color in list(Color)]])
        # _test_run(empty_script, map, exit_on_tick=None, is_render=True)
        _test_run(empty_script, map, exit_on_tick=1)


if __name__ == "__main__":
    unittest.main()
