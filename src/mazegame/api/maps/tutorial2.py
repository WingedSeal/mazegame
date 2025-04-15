from ...color import Color
from ...map import (
    ColoredBlock,
    CustomMapType,
    Door,
    Exit,
    Key,
    Map,
    Block,
    Player,
    Spike,
)


def _get_map():
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
    return (
        [TUTORIAL2_1, TUTORIAL2_2, TUTORIAL2_3, TUTORIAL2_4],
        """The exit will always be above purple block!
(Technically, you can check for exit. But please don't do that~)""",
    )


TUTORIAL2: CustomMapType = _get_map

# def script():
#     while get_color(RIGHT) != PURPLE:
#         move(UP)
#     move(UP)
#     move(RIGHT)
