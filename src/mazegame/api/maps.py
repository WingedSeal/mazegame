from ..direction import Direction
from ..color import Color
from ..map import ColoredFloor, Enemy, Map, Block, Player

TEST_MAP_ENEMY = Enemy(
    [
        Direction.RIGHT,
        Direction.RIGHT,
        Direction.LEFT,
        Direction.LEFT,
    ],
    chance_to_move=0.5,
)

TEST_MAP = Map(
    [
        [TEST_MAP_ENEMY, None, None, None, Block(), None, Block()],
        [None, None, None, None, Block(), None, Block()],
        [None, None, None, ColoredFloor(Color.BLUE), Player(), None, Player()],
    ]
)

__all__ = ["TEST_MAP"]
