from ...map_maker import map_maker
from ...color import Color
from ...map import CustomMapType, ColoredFloor, Map, Spike, Block


def _get_map():
    colors = Color.get_unique_colors(3)
    colors2 = Color.get_unique_colors(6)
    PRACTICE4_1 = Map(
        map_maker(
            f"""
XXXXXXXXXX
XXXXXXXXSX
XXXXXXXX X
XS _    _X
XXX XXXX X
XXX XXXXEX
XXX XXXXXX
XXX_XXXXXX
XXX_XXXXXX
XXX XXXXXX
XXXPXXXXXX
XXXXXXXXXX
""",
            [
                ColoredFloor(colors[0]),
                ColoredFloor(colors[1]),
                ColoredFloor(colors[1]),
                ColoredFloor(colors[0]),
            ],
        )
    )

    PRACTICE4_2 = Map(
        map_maker(
            f"""
XXXXXXXXXX
XSXXXXXXXX
X XXXXXXXX
X_    _ SX
X XXXX XXX
XEXXXX XXX
XXXXXX XXX
XXXXXX_XXX
XXXXXX_XXX
XXXXXX XXX
XXXXXXPXXX
XXXXXXXXXX
""",
            [
                ColoredFloor(colors2[2]),
                ColoredFloor(colors2[3]),
                ColoredFloor(colors2[3]),
                ColoredFloor(colors2[2]),
            ],
        )
    )
    return (
        [PRACTICE4_1, PRACTICE4_2],
        "In the first colour pair, if the color of the tiles match go right. If not, go left. In the second colour pair, if the colour match, go up. Else go down",
    )


PRACTICE4: CustomMapType = _get_map

# def script():
#     move(UP)
#     move(UP)
#     c1 = get_color()
#     move(UP)
#     c2 = get_color()
#     for i in range(4):
#         move(UP)
#     if c1 == get_color():
#         for i in range(5):
#             move(RIGHT)
#     else:
#         for i in range(5):
#             move(LEFT)
#     if c2 == get_color():
#         for i in range(5):
#             move(UP)
#     else:
#         for i in range(5):
#             move(DOWN)
