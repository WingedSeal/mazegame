from ...map_maker import map_maker
from ...color import Color
from ...map import CustomMapType, ColoredFloor, Map, Lock, Door


def _get_map():
    color0, color1, color2, color3, color4 = Color.get_unique_colors(5)
    PRACTICE4_1 = Map(
        map_maker(
            f"""
XXXXXXXXXX
XXXXXXXXEX
XXXXXXXX_X
XXXXXXXX_X
X___    _X
XXX XXXX_X
XXX XXXX_X
XXX XXXXXX
XXX_XXXXXX
XXX_XXXXXX
XXX XXXXXX
XXXPXXXXXX
XXXXXXXXXX
""",
            [
                Lock(color0),
                Door(color0, open=True),
                Lock(color0),
                Door(color0, open=True),
                ColoredFloor(color1),
                ColoredFloor(color2),
                Door(color0, open=True),
                Lock(color0),
                ColoredFloor(color2),
                ColoredFloor(color1),
            ],
        )
    )

    PRACTICE4_2 = Map(
        map_maker(
            f"""
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXX_X
XXXXXXXX_X
X___    _X
XXX XXXX_X
XXX XXXX_X
XXX XXXXEX
XXX_XXXXXX
XXX_XXXXXX
XXX XXXXXX
XXXPXXXXXX
XXXXXXXXXX
""",
            [
                Lock(color0),
                Door(color0, open=True),
                Lock(color0),
                Door(color0, open=True),
                ColoredFloor(color1),
                ColoredFloor(color2),
                Door(color0, open=True),
                Lock(color0),
                ColoredFloor(color3),
                ColoredFloor(color1),
            ],
        )
    )

    PRACTICE4_3 = Map(
        map_maker(
            f"""
XXXXXXXXXX
XEXXXXXXXX
X_XXXXXXXX
X_XXXXXXXX
X_    ___X
X_XXXX XXX
X_XXXX XXX
XXXXXX XXX
XXXXXX_XXX
XXXXXX_XXX
XXXXXX XXX
XXXXXXPXXX
XXXXXXXXXX
""",
            [
                Lock(color0),
                Door(color0, open=True),
                ColoredFloor(color1),
                ColoredFloor(color2),
                Lock(color0),
                Door(color0, open=True),
                Door(color0, open=True),
                Lock(color0),
                ColoredFloor(color1),
                ColoredFloor(color3),
            ],
        )
    )

    PRACTICE4_4 = Map(
        map_maker(
            f"""
XXXXXXXXXX
X_XXXXXXXX
X_XXXXXXXX
X_    ___X
X_XXXX XXX
X_XXXX XXX
XEXXXX XXX
XXXXXX_XXX
XXXXXX_XXX
XXXXXX XXX
XXXXXXPXXX
XXXXXXXXXX
""",
            [
                Lock(color0),
                Door(color0, open=True),
                ColoredFloor(color1),
                ColoredFloor(color2),
                Lock(color0),
                Door(color0, open=True),
                Door(color0, open=True),
                Lock(color0),
                ColoredFloor(color3),
                ColoredFloor(color4),
            ],
        )
    )
    return (
        [PRACTICE4_1, PRACTICE4_2, PRACTICE4_3, PRACTICE4_4],
        """If the first and third colored floor have the same color, go right. Otherwise, go left.
Then if the second and fourth colored floor have the same color, go up. Otherwise, go down.
(Color ordered by distance from the player)""",
    )


PRACTICE4: CustomMapType = _get_map

# def script():
#     move(UP)
#     move(UP)
#     color1 = get_color()
#     move(UP)
#     color3 = get_color()
#     for _ in range(4):
#         move(UP)
#     if color1 == get_color():
#         for _ in range(5):
#             move(RIGHT)
#     else:
#         for _ in range(5):
#             move(LEFT)
#     if color3 == get_color():
#         for _ in range(5):
#             move(UP)
#     else:
#         for _ in range(5):
#             move(DOWN)
