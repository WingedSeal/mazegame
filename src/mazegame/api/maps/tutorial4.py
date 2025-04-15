from ...color import Color
from ...direction import Direction
from ...map import Block, CustomMapType, Door, Enemy, Exit, Key, Map, Player


def _get_map():

    color = Color.get_unique_colors(1)[0]

    TUTORIAL4_1 = Map(
        [
            [Block(), Exit(), Block()],
            [Block(), Door(color), Block()],
            [Block(), Player(), Block()],
            [Block(), Key(color), Block()],
        ]
    )
    return ([TUTORIAL4_1], "Touching the key will open all doors with the same color.")


TUTORIAL4: CustomMapType = _get_map

# def script():
#     move(DOWN)
#     for _ in range(3):
#         move(UP)
