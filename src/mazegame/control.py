import threading
from typing import TYPE_CHECKING
from threading import Lock

from .map import Map

if TYPE_CHECKING:
    from .game import Game


class Control:
    control_event = threading.Event()

    def __init__(self, map: Map, game: "Game") -> None:
        self.game = game
        self.player_positions = map.get_player_positions()

    def _move(self, dx: int, dy: int) -> None:
        self.control_event.wait()
        self.game.next_moves = [
            (player_pos[0], player_pos[1], dx, dy)
            for player_pos in self.player_positions
        ]
        self.player_positions = []
        self.control_event.clear()
        self.game.game_event.set()

    def test_run(self):
        self._move(-1, 0)
        self._move(-1, 0)
        self._move(-1, 0)
        self._move(0, -1)
        self.game.is_control_alive = False
