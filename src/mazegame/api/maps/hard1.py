from ...direction import Direction
from ...color import Color
from ...map import ColoredFloor, Enemy, Map, Block, Player

ENEMY = Enemy(
    [Direction.UP] * 10 + [Direction.DOWN] * 10,
    chance_to_move=0.8,
)

HARD1 = Map(
    [
        [Block(), None, None, Block()],
        [Block(), None, Block(), Block()],
        [Block(), None, Block(), Block()],
        [Block(), None, Block(), Block()],
        [Block(), None, Block(), Block()],
        [Block(), None, Block(), Block()],
        [Block(), None, None, Block()],
        [Block(), None, Block(), Block()],
        [Block(), None, Block(), Block()],
        [Block(), None, Block(), Block()],
        [Block(), ENEMY, Block(), Block()],
        [Block(), Player(), Block(), Block()],
    ]
)
