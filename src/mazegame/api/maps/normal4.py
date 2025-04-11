from ...direction import Direction
from ...color import Color
from ...map import Door, Enemy, Exit, Key, Map, Block, Player, Lock

color1, color2 = Color.get_unique_colors(2)
KEY1 = Key(color1)
LOCK2 = Lock(color2)
DOOR1 = Door(color1)
DOOR2 = Door(color2, open=True)
ENEMY1 = Enemy([Direction.UP] * 5 + [Direction.DOWN] * 7 + [Direction.UP] * 2)
ENEMY2 = Enemy(
    [Direction.HALT] * 12 + [Direction.DOWN] + [Direction.HALT] * 10 + [Direction.UP]
)
# fmt: off
NORMAL4 = Map(
    [
        [Block(), None,     Block(), None],
        [Block(), DOOR2,    Block(), None],
        [Block(), KEY1,     Block(), None],
        [Block(), None,     Block(), None],
        [Block(), None,     Block(), Exit()],
        [Block(), ENEMY1,   Block(), None],
        [Block(), LOCK2,    Block(), None],
        [Block(), Player(), ENEMY2,  DOOR1],
        [Block(), Block(),  None,    Block()]
    ]
)
# fmt: on
