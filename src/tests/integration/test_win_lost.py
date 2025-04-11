import sys

from mazegame.direction import Direction
from mazegame.game import GameState  # noqa

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


class TestWinLost(unittest.TestCase):
    def setUp(self) -> None:
        import os

        os.environ["SDL_VIDEODRIVER"] = "dummy"
        return super().setUp()

    def test_win(self) -> None:
        map = Map([[Player(), Exit()]])

        def script():
            move(RIGHT)

        game = _test_run(script, map, exit_on_tick=1)
        self.assertEqual(game.state, GameState.VICTORY)

    def test_run_into_enemy(self) -> None:
        map = Map([[Player(), Enemy(path=[])]])

        def script():
            move(RIGHT)

        game = _test_run(script, map, exit_on_tick=1)
        self.assertEqual(game.state, GameState.GAME_OVER)

    def test_enemy_run_into_player(self) -> None:
        map = Map([[Player(), Enemy(path=[Direction.LEFT])]])

        def script():
            return

        game = _test_run(script, map, exit_on_tick=1)
        self.assertEqual(game.state, GameState.GAME_OVER)
