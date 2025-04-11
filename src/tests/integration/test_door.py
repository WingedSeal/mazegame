import sys  # noqa

sys.path.append("./src")  # noqa

import os
import unittest
from mazegame import *
from mazegame.color import Color
from mazegame.map import (
    Block,
    ColoredBlock,
    Lock,
    Door,
    DoorFrame,
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


class TestDoor(unittest.TestCase):

    def test_door_open(self):
        map = Map(
            [
                [
                    Door(Color.BLUE),
                    Door(Color.RED),
                    Door(Color.RED),
                    Player(),
                    Key(Color.RED),
                ]
            ]
        )

        def script():
            move(RIGHT)

        game = _test_run(script, map, exit_on_tick=1)
        self.assertIsInstance(game.map.map[0][0], Door)
        self.assertIsInstance(game.map.map[0][1], DoorFrame)
        self.assertIsInstance(game.map.map[0][2], DoorFrame)

    def test_door_lock(self):
        map = Map(
            [
                [
                    Door(Color.BLUE, open=True),
                    Door(Color.RED, open=True),
                    Door(Color.RED, open=True),
                    Player(),
                    Lock(Color.RED),
                ]
            ]
        )

        def script():
            move(RIGHT)

        game = _test_run(script, map, exit_on_tick=1)
        self.assertIsInstance(game.map.map[0][0], DoorFrame)
        self.assertIsInstance(game.map.map[0][1], Door)
        self.assertIsInstance(game.map.map[0][2], Door)

    def test_door_same_state(self):
        map = Map(
            [
                [
                    Door(Color.BLUE, open=True),
                    Door(Color.RED, open=True),
                    Door(Color.RED, open=True),
                    Player(),
                    Key(Color.RED),
                ],
                [
                    Door(Color.BLUE),
                    Door(Color.GREEN),
                    Door(Color.GREEN),
                    Player(),
                    Lock(Color.GREEN),
                ],
            ]
        )

        def script():
            move(RIGHT)

        game = _test_run(script, map, exit_on_tick=1)
        for x in range(3):
            self.assertIsInstance(game.map.map[0][x], DoorFrame)
            self.assertIsInstance(game.map.map[1][x], Door)


if __name__ == "__main__":
    unittest.main()
