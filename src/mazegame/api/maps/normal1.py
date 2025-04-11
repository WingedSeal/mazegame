from ...direction import Direction
from ...color import Color
from ...map import Door, Enemy, Exit, Key, Map, Block, Player, Spike

KEY1 = Key(Color.LIGHT_BLUE)
KEY2 = Key(Color.GREEN)
DOOR1 = Door(Color.LIGHT_BLUE)
DOOR2 = Door(Color.GREEN)
# fmt: off
NORMAL1 = Map(
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
