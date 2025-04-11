import sys  # noqa

sys.path.append("./src")  # noqa

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


class TestBasicRender(unittest.TestCase):
    def test_all_tile(self):
        map = Map(
            [
                [Block(), None, Spike()],
                [Player(), Enemy(path=[]), Door(Color.RED)],
                [Exit(), ColoredBlock(Color.RED), ColoredFloor(Color.RED)],
                [Key(Color.RED), None, None],
            ]
        )
        _test_run(empty_script, map, exit_on_tick=1)
