from ...direction import Direction
from ...color import Color
from ...map import ColoredBlock, Door, Enemy, Exit, Key, Map, Block, Player, Spike

KEY1 = Key(Color.LIGHT_BLUE)
KEY2 = Key(Color.GREEN)
DOOR1 = Door(Color.LIGHT_BLUE)
DOOR2 = Door(Color.GREEN)
# fmt: off
EXAMPLE2_1 = Map(
    [
        [Block(), None,     Spike()],
        [Block(), None,     Spike()],
        [Block(), None,     Spike()],
        [Block(), None,     Exit()],
        [Block(), Player(), ColoredBlock(Color.PURPLE)]
    ]
)
EXAMPLE2_2 = Map(
    [
        [Block(), None,     Spike()],
        [Block(), None,     Spike()],
        [Block(), None,     Exit()],
        [Block(), None,     ColoredBlock(Color.PURPLE)],
        [Block(), Player(), Spike()]
    ]
)
EXAMPLE2_3 = Map(
    [
        [Block(), None,     Spike()],
        [Block(), None,     Exit()],
        [Block(), None,     ColoredBlock(Color.PURPLE)],
        [Block(), None,     Spike()],
        [Block(), Player(), ColoredBlock(Color.LIGHT_BLUE)]
    ]
)
EXAMPLE2_4 = Map(
    [
        [Block(), None,     Exit()],
        [Block(), None,     ColoredBlock(Color.PURPLE)],
        [Block(), None,     ColoredBlock(Color.LIGHT_BLUE)],
        [Block(), None,     Spike()],
        [Block(), Player(), Spike()]
    ]
)
# fmt: on

EXAMPLE2 = [EXAMPLE2_1, EXAMPLE2_2, EXAMPLE2_3, EXAMPLE2_4]


# def script():
#     while get_color(RIGHT) != PURPLE:
#         move(UP)
#     move(UP)
#     move(RIGHT)
