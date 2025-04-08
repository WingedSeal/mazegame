from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .game import Game


class Control:
    def __init__(self, player_positions: list[tuple[int, int]]) -> None:
        self.player_positions = player_positions
        self.map = map

    def _move(self, dx: int, dy: int, game: "Game") -> None:
        for player_pos in self.player_positions:
            game.try_move_tile(player_pos[0], player_pos[1], dx, dy)
