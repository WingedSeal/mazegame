from ..direction import Direction
from ..map import Enemy, Map, Block, Player

TEST_MAP_ENEMY = Enemy(
    [
        Direction.RIGHT,
        Direction.RIGHT,
        Direction.LEFT,
        Direction.LEFT,
    ]
)

TEST_MAP = Map(
    [
        [TEST_MAP_ENEMY, None, None, None, Block(), None, Block()],
        [None, None, None, None, Block(), None, Block()],
        [None, None, None, None, Player(), None, Player()],
    ]
)

__all__ = ["TEST_MAP"]
