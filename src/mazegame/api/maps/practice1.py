from ...map_maker import map_maker
from ...color import Color
from ...map import CustomMapType, Door, Key, Map


def _get_map():
    color1, color2 = Color.get_unique_colors(2)
    PRACTICE1_1 = Map(
        map_maker(
            f"""
XXXXXXXXX
XXXEXXSXX
XXX_XX  X
XX     SX
XX SXXPXX
XX _   XX
XXXXXXXXX
XXXXXXXXX
XXXX  _XX
XXS _X_XX
X      XX
XX XXX XX
XX XP  XX
XX XS  XX
XX    XXX
XXXXXXXXX
""",
            [Door(color1), Key(color2), Key(color1), Door(color1), Door(color2)],
        )
    )
    return ([PRACTICE1_1], "There are 2 players.")


PRACTICE1: CustomMapType = _get_map

# def script():
#     move(RIGHT)
#     move(DOWN)
#     move(DOWN)
#     for _ in range(4):
#         move(LEFT)
#     for _ in range(4):
#         move(UP)
#     for _ in range(4):
#         move(RIGHT)
#     move(UP)
#     move(RIGHT)
#     move(UP)
#     move(LEFT)
#     move(DOWN)
#     for _ in range(3):
#         move(LEFT)
#     move(UP)
#     move(UP)
