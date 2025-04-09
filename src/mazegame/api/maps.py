from ..direction import Direction
from ..color import Color
from ..map import ColorFloor, Enemy, Map, Block, Player

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
        [None, None, None, ColorFloor(Color.BLUE), Player(), None, Player()],
    ]
)

__all__ = ["TEST_MAP"]
