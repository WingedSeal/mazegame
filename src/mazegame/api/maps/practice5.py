from ...map_maker import map_maker
from ...color import Color
from ...map import CustomMapType, Door, Map, Lock, ColoredBlock, ColoredFloor


def _get_map():
    color1, color2, color3, color4, color5 = Color.get_unique_colors(5)
    PRACTICE5_2 = Map(
        map_maker(
            f"""
XXXXXX
XX__ X
XXX_ X
XE__ X
XXX_ X
XX__ X
XXX_ X
XX__ X
XXX_ X
XXXX X
XXXX_X
XXXXPX
XXXXXX
""",
            [
                Lock(color1),
                Door(color1, open=True),
                ColoredBlock(color2),
                Lock(color1),
                Door(color1, open=True),
                ColoredBlock(color3),
                Lock(color1),
                Door(color1, open=True),
                ColoredBlock(color4),
                Lock(color1),
                Door(color1, open=True),
                ColoredBlock(color5),
                ColoredFloor(color3),
            ],
        )
    )
    PRACTICE5_1 = Map(
        map_maker(
            f"""
XXXXXX
XE__ X
XXX_ X
XX__ X
XXX_ X
XX__ X
XXX_ X
XX__ X
XXX_ X
XXXX X
XXXX_X
XXXXPX
XXXXXX
""",
            [
                Lock(color1),
                Door(color1, open=True),
                ColoredBlock(color2),
                Lock(color1),
                Door(color1, open=True),
                ColoredBlock(color3),
                Lock(color1),
                Door(color1, open=True),
                ColoredBlock(color4),
                Lock(color1),
                Door(color1, open=True),
                ColoredBlock(color5),
                ColoredFloor(color2),
            ],
        )
    )
    PRACTICE5_3 = Map(
        map_maker(
            f"""
XXXXXX
XX__ X
XXX_ X
XX__ X
XXX_ X
XE__ X
XXX_ X
XX__ X
XXX_ X
XXXX X
XXXX_X
XXXXPX
XXXXXX
""",
            [
                Lock(color1),
                Door(color1, open=True),
                ColoredBlock(color2),
                Lock(color1),
                Door(color1, open=True),
                ColoredBlock(color3),
                Lock(color1),
                Door(color1, open=True),
                ColoredBlock(color4),
                Lock(color1),
                Door(color1, open=True),
                ColoredBlock(color5),
                ColoredFloor(color4),
            ],
        )
    )

    PRACTICE5_4 = Map(
        map_maker(
            f"""
XXXXXX
XX__ X
XXX_ X
XX__ X
XXX_ X
XX__ X
XXX_ X
XE__ X
XXX_ X
XXXX X
XXXX_X
XXXXPX
XXXXXX
""",
            [
                Lock(color1),
                Door(color1, open=True),
                ColoredBlock(color2),
                Lock(color1),
                Door(color1, open=True),
                ColoredBlock(color3),
                Lock(color1),
                Door(color1, open=True),
                ColoredBlock(color4),
                Lock(color1),
                Door(color1, open=True),
                ColoredBlock(color5),
                ColoredFloor(color5),
            ],
        )
    )
    return (
        [PRACTICE5_1, PRACTICE5_2, PRACTICE5_3, PRACTICE5_4],
        "The exit is above the colored wall with the same color as the colored floor.",
    )


PRACTICE5: CustomMapType = _get_map

# def script():
#     move(UP)
#     color = get_color()
#     while get_color(LEFT) != color:
#         move(UP)
#     move(UP)
#     move(LEFT)
#     move(LEFT)
#     move(LEFT)
