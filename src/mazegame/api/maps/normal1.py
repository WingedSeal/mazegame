from ...color import Color
from ...map import CustomMapType, Door, Exit, Key, Map, Block, Player, Spike


def _get_map():
    KEY1 = Key(Color.LIGHT_BLUE)
    KEY2 = Key(Color.GREEN)
    DOOR1 = Door(Color.LIGHT_BLUE)
    DOOR2 = Door(Color.GREEN)
    # fmt: off
    NORMAL1_1 = Map(
        [
            [Block(), Block(), Block(), Block(),  Block(), Block(), Block(), Block(),  Block()],
            [None,    Block(), Block(), Block(),  Block(), Block(), Block(), Block(),  Spike()],
            [DOOR2,   None,    None,    Player(), DOOR1,   Exit(),  Block(), Player(), None   ],
            [None,    Block(), Block(), KEY2,     Block(), Block(), Block(), Spike(),  Block()],
            [KEY1,    Block(), Block(), Block(),  Block(), Block(), Block(), Block(),  Block()],
            [Block(), Block(), Block(), Block(),  Block(), Block(), Block(), Block(),  Block()]
        ]
    )
    # fmt: on
    return ([NORMAL1_1], "Beware of the spike!")


NORMAL1: CustomMapType = _get_map
# def script():
#     move(RIGHT)
#     move(DOWN)
#     move(LEFT)
#     move(UP)
#     for _ in range(3):
#         move(LEFT)
#     move(UP)
#     move(RIGHT)
#     for _ in range(3):
#         move(DOWN)
#     move(LEFT)
#     for _ in range(2):
#         move(UP)
#     for _ in range(5):
#         move(RIGHT)
