import sys  # noqa

sys.path.append("./src")  # noqa

import unittest
from mazegame import *
from mazegame.color import Color
from mazegame.map import Block, ColoredBlock, Exit, Map, Player, Spike
from mazegame.api.run import _test_run


def empty_script():
    pass


class TestBasicRender(unittest.TestCase):
    def test_all_tile(self):
        map = Map(
            [
                [Block(), None, Exit()],
                [Block(), None, ColoredBlock(Color.PURPLE)],
                [Block(), None, ColoredBlock(Color.DEEP_BLUE)],
                [Block(), None, Spike()],
                [Block(), Player(), Spike()],
            ]
        )
        game = _test_run(empty_script, map)
        print(game)
