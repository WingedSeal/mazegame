import random
import threading
from typing import Callable

from ..direction import Direction
from ..game import Game
from ..map import Map, Tile
from .game_obj import get_game
from . import game_obj


def move(direction: Direction) -> None:
    """Move player in a direction"""
    get_game().control.move(direction)


def get_tile(
    direction: Direction = Direction.HALT, player_index: int = 0
) -> Tile | None:
    """
    Get the tile on a direction compared to a player

    :param direction: Which direction to look for tile, use Halt to get the tile player is on, defaults to Direction.Halt
    :param player_index: Which player to get tile from, defaults to 0
    :return: Tile or None
    """
    return get_game().get_tile(direction, player_index)


def run(script: Callable[[], None], map: Map | list[Map]) -> None:
    if isinstance(map, list):
        map = random.choice(map)
    game_obj.game = Game(map)

    def updated_script() -> None:
        get_game().control.pre_run()
        script()
        get_game().control.post_run()

    script_thread = threading.Thread(target=updated_script, daemon=True)
    script_thread.start()
    get_game().run()
