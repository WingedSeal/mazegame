import sys


sys.path.append("./src")  # noqa

import os
import unittest
from mazegame import *
from mazegame.direction import Direction
from mazegame.game import Game, GameState
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


class TestEnemy(unittest.TestCase):

    def test_path(self):
        map = Map(
            [
                [
                    Enemy(
                        path=[
                            Direction.RIGHT,
                            Direction.RIGHT,
                            Direction.DOWN,
                            Direction.LEFT,
                            Direction.LEFT,
                        ]
                    ),
                    None,
                    None,
                ],
                [None, None, None],
            ]
        )
        game = _test_run(empty_script, map, exit_on_tick=5)
        self.assertIsInstance(game.map.map[1][0], Enemy)


if __name__ == "__main__":

    unittest.main()
