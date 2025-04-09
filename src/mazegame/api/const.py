from ..map import Block, ColoredFloor, Enemy
from ..color import Color
from ..direction import Direction

RED = Color.RED
BLUE = Color.BLUE
GREEN = Color.GREEN
LEFT = Direction.LEFT
RIGHT = Direction.RIGHT
DOWN = Direction.DOWN
UP = Direction.UP
HALT = Direction.HALT

BLOCK = Block.__name__
ENEMY = Enemy.__name__
COLORED_FLOOR = ColoredFloor.__name__

__all__ = [
    "RED",
    "BLUE",
    "GREEN",
    "LEFT",
    "RIGHT",
    "DOWN",
    "UP",
    "DOWN",
    "HALT",
    "BLOCK",
    "ENEMY",
    "COLORED_FLOOR",
]
