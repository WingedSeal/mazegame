import random
from ...map_maker import map_maker
from ...color import Color
from ...map import CustomMapType, Map, ColoredFloor, Door, Lock


def _get_map():
    door_color = Color.get_unique_colors(1)[0]

    red_count = random.randrange(3, 9 + 1, 2)
    colors = Color.get_unique_colors(9 - red_count, [Color.RED])
    floors = [
        *(ColoredFloor(Color.RED) for _ in range(red_count)),
        *(ColoredFloor(color) for color in colors),
    ]
    random.shuffle(floors)
    HARD2_ODD = Map(
        map_maker(
            f"""
XXXXXXXXXXX
XP ___XXXXX
XXX___XXXXX
XXX___    X
XXXXXXX_X_X
XXXXXXX_X_X
XXXXXXXSXEX
XXXXXXXXXXX
""",
            [
                *floors,
                Door(door_color, open=True),
                Door(door_color, open=True),
                Lock(door_color),
                Lock(door_color),
            ],
        )
    )

    red_count = random.randrange(2, 8 + 1, 2)
    colors = Color.get_unique_colors(9 - red_count, [Color.RED])
    floors = [
        *(ColoredFloor(Color.RED) for _ in range(red_count)),
        *(ColoredFloor(color) for color in colors),
    ]
    random.shuffle(floors)
    HARD2_EVEN = Map(
        map_maker(
            f"""
XXXXXXXXXXX
XP ___XXXXX
XXX___XXXXX
XXX___    X
XXXXXXX_X_X
XXXXXXX_X_X
XXXXXXXEXSX
XXXXXXXXXXX
""",
            [
                *floors,
                Door(door_color, open=True),
                Door(door_color, open=True),
                Lock(door_color),
                Lock(door_color),
            ],
        )
    )

    return (
        [HARD2_EVEN, HARD2_ODD],
        """Count the number of red tiles. And go to the first exit if it's even. Go to the second exit if it's odd.
Use 'a % n' to get the remainder of a / n""",
    )


HARD2: CustomMapType = _get_map
