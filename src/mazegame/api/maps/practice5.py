from ...map_maker import map_maker
from ...color import Color
from ...map import CustomMapType, Door, Map, Lock, ColoredBlock, ColoredFloor


def _get_map():
    color1, color2, color3, color4, color5, color6 = Color.get_unique_colors(6)
    PRACTICE5_2 = Map(
        map_maker(
            f"""
XXXXX
X__ X
XX_ X
XE_ X
XX_ X
X__ X
XX_ X
X__ X
XX_ X
XXX X
XXX_X
XXXPX
XXXXX
""",
            [
                Lock(color1),
                Door(color1, open=True),
                ColoredBlock(color2),
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
XXXXX
XE_ X
XX_ X
X__ X
XX_ X
X__ X
XX_ X
X__ X
XX_ X
XXX X
XXX_X
XXXPX
XXXXX
""",
            [
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
XXXXX
X__ X
XX_ X
X__ X
XX_ X
XE_ X
XX_ X
X__ X
XX_ X
XXX X
XXX_X
XXXPX
XXXXX
""",
            [
                Lock(color1),
                Door(color1, open=True),
                ColoredBlock(color2),
                Lock(color1),
                Door(color1, open=True),
                ColoredBlock(color3),
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
XXXXX
X__ X
XX_ X
X__ X
XX_ X
X__ X
XX_ X
XE_ X
XX_ X
XXX X
XXX_X
XXXPX
XXXXX
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
                Door(color1, open=True),
                ColoredBlock(color5),
                ColoredFloor(color5),
            ],
        )
    )
    return (
        [PRACTICE5_1, PRACTICE5_2, PRACTICE5_3, PRACTICE5_4],
        "There are 2 players.",
    )


PRACTICE5: CustomMapType = _get_map

# def script():
#     move(UP)
#     c1 = get_color()
#     for i in range(9):
#         move(UP)
#         if get_color(LEFT) == c1:
#             move(UP)
#             move(LEFT)
#             move(LEFT)
