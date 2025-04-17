from ...direction import Direction
from ...color import Color
from ...map import CustomMapType, Door, Enemy, Exit, Key, Map, Block, Player, Spike


def _get_map():

    NIGHTMARE2_1 = Map([[Player(), Spike(), Exit()]])

    return (
        [NIGHTMARE2_1],
        "You may import anything from the library. But do not modify the map ('NIGHTMARE2' function). Only write code in script function.\n"
        "Try to modify interaction behavior of the spike object gotten from get_tile(). You might need isinstance to get intellisense working.\n"
        "Walk over that spike!, somehow.",
    )


NIGHTMARE2: CustomMapType = _get_map


# Scroll down for solution
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# from mazegame.map import Spike


# def script():
#     def interacted_with(other_tile, game) -> None:
#         pass

#     tile = get_tile(RIGHT)
#     if not isinstance(tile, Spike):
#         raise Exception()
#     tile.interacted_with = interacted_with
#     # tile.interacted_with = lambda other_tile, game: None
#     move(RIGHT)
#     move(RIGHT)
