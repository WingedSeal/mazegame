import threading
from typing import TYPE_CHECKING

from .direction import Direction


from .map import Map

if TYPE_CHECKING:
    from .game import Game


class Control:
    control_event = threading.Event()

    def __init__(self, map: Map, game: "Game") -> None:
        self.control_event.clear()
        self.game = game
        self.player_positions = map.get_player_positions()

    def move(self, direction: Direction) -> None:
        match direction:
            case Direction.LEFT:
                self._move(-1, 0)
            case Direction.RIGHT:
                self._move(1, 0)
            case Direction.UP:
                self._move(0, -1)
            case Direction.DOWN:
                self._move(0, 1)
            case Direction.HALT:
                self._halt()
            case _:
                raise ValueError("Invalid Direction")

    def _move(self, dx: int, dy: int) -> None:
        self.game.next_moves = [
            (player_pos[0], player_pos[1], dx, dy)
            for player_pos in self.player_positions
        ]
        self.player_positions = []
        self.control_event.clear()
        self.game.game_event.set()
        self.control_event.wait()

    def _halt(self) -> None:
        self.control_event.clear()
        self.game.game_event.set()
        self.control_event.wait()

    def pre_run(self) -> None:
        self.control_event.wait()

    def post_run(self) -> None:
        self.control_event.clear()
        self.game.game_event.set()
        self.game.is_control_alive = False
