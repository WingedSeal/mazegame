import os
import random
import threading
from typing import Callable

from ..color import Color
from ..direction import Direction
from ..game import Game
from ..map import GetColor, Map, Tile
from .game_obj import get_game
from . import game_obj


def move(direction: Direction) -> None:
    """Move player in a direction"""
    get_game().control.move(direction)


def wait() -> None:
    """Consume a turn, but doesn't move (Same as `move(HALT)`)"""
    get_game().control.move(Direction.HALT)


def halt() -> None:
    """Consume a turn, but doesn't move (Same as `move(HALT)`)"""
    get_game().control.move(Direction.HALT)


def get_tile(
    direction: Direction = Direction.HALT, player_index: int = 0
) -> Tile | None:
    """
    Get the tile in a direction compared to a player

    :param direction: Which direction to look for tile, use Halt to get the tile player is on, defaults to Direction.Halt
    :param player_index: Which player to get tile from, defaults to 0
    :return: Tile or None
    """
    return get_game().get_tile(direction, player_index)


def get_color(
    direction: Direction = Direction.HALT, player_index: int = 0
) -> Color | None:
    """
    Get the color of the tile in a direction compared to a player

    :param direction: Which direction to look for tile, use Halt to get the tile player is on, defaults to Direction.Halt
    :param player_index: Which player to get tile from, defaults to 0
    :return: Tile or None
    """
    tile = get_game().get_tile(direction, player_index)
    if not isinstance(tile, GetColor):
        return None

    return tile.get_color()


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


def _test_run(
    script: Callable[[Game], None],
    map: Map | list[Map],
    *,
    exit_on_tick: int | None = None,
    mspt: int | None = 1,
    is_render: bool = False
) -> Game:
    if not is_render:
        os.environ["SDL_VIDEODRIVER"] = "dummy"

    if isinstance(map, list):
        map = random.choice(map)
    game = Game(map)
    game._exit_on_tick = exit_on_tick
    if mspt is not None:
        game.MSPT = mspt  # type: ignore
    game_obj.game = game

    def updated_script() -> None:
        get_game().control.pre_run()
        script(game)
        get_game().control.post_run()

    script_thread = threading.Thread(target=updated_script, daemon=True)
    script_thread.start()
    game.run()
    if not is_render:
        del os.environ["SDL_VIDEODRIVER"]
    return game
