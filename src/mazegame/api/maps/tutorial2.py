from ...color import Color
from ...map import ColoredBlock, Door, Exit, Key, Map, Block, Player, Spike

# fmt: off
TUTORIAL2_1 = Map(
    [
        [Block(), None,     Spike()],
        [Block(), None,     Spike()],
        [Block(), None,     Spike()],
        [Block(), None,     Exit()],
        [Block(), Player(), ColoredBlock(Color.PURPLE)]
    ]
)
TUTORIAL2_2 = Map(
    [
        [Block(), None,     Spike()],
        [Block(), None,     Spike()],
        [Block(), None,     Exit()],
        [Block(), None,     ColoredBlock(Color.PURPLE)],
        [Block(), Player(), Spike()]
    ]
)
TUTORIAL2_3 = Map(
    [
        [Block(), None,     Spike()],
        [Block(), None,     Exit()],
        [Block(), None,     ColoredBlock(Color.PURPLE)],
        [Block(), None,     Spike()],
        [Block(), Player(), Spike()]
    ]
)
TUTORIAL2_4 = Map(
    [
        [Block(), None,     Exit()],
        [Block(), None,     ColoredBlock(Color.PURPLE)],
        [Block(), None,     Spike()],
        [Block(), None,     Spike()],
        [Block(), Player(), Spike()]
    ]
)
# fmt: on

TUTORIAL2 = [TUTORIAL2_1, TUTORIAL2_2, TUTORIAL2_3, TUTORIAL2_4]


# def script():
#     while get_color(RIGHT) != PURPLE:
#         move(UP)
#     move(UP)
#     move(RIGHT)
