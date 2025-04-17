from ...direction import Direction
from ...color import Color
from ...map import CustomMapType, Door, Enemy, Exit, Key, Map, Block, Player


def _get_map():

    NIGHTMARE1_1 = Map([[Player(), Key(Color.RED), Door(Color.BLUE), Exit()]])

    return (
        [NIGHTMARE1_1],
        "You may import anything from the library. But do not modify the map ('NIGHTMARE_1' function). Only write code in script function.\n"
        "Try to modify color of the key object gotten from get_tile(). You might need isinstance to get intellisense working.\n"
        "The color may not update on the screen. That's normal.",
    )


NIGHTMARE1: CustomMapType = _get_map


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
# from mazegame.color import Color
# from mazegame.map import Key


# def script():
#     tile = get_tile(RIGHT)
#     if not isinstance(tile, Key):
#         raise Exception()
#     tile.color = Color.BLUE
#     for _ in range(3):
#         move(RIGHT)
