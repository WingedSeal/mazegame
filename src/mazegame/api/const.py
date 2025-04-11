from ..map import (
    Block,
    ColoredBlock,
    ColoredFloor,
    Door,
    DoorFrame,
    Enemy,
    Exit,
    Key,
    Spike,
)
from ..color import Color
from ..direction import Direction

RED = Color.RED
ORANGE = Color.ORANGE
YELLOW = Color.YELLOW
GREEN = Color.GREEN
LIGHT_BLUE = Color.LIGHT_BLUE
BLUE = Color.BLUE
PURPLE = Color.PURPLE

LEFT = Direction.LEFT
RIGHT = Direction.RIGHT
DOWN = Direction.DOWN
UP = Direction.UP
HALT = Direction.HALT

BLOCK = Block.__name__
ENEMY = Enemy.__name__
COLORED_FLOOR = ColoredFloor.__name__
COLORED_BLOCK = ColoredBlock.__name__
SPIKE = Spike.__name__
EXIT = Exit.__name__
DOOR = Door.__name__
DOOR_FRAME = DoorFrame.__name__
KEY = Key.__name__


__all__ = [
    "RED",
    "ORANGE",
    "YELLOW",
    "GREEN",
    "BLUE",
    "LIGHT_BLUE",
    "PURPLE",
    "LEFT",
    "RIGHT",
    "DOWN",
    "UP",
    "HALT",
    "BLOCK",
    "ENEMY",
    "COLORED_FLOOR",
    "COLORED_BLOCK",
    "SPIKE",
    "EXIT",
    "DOOR",
    "DOOR_FRAME",
    "KEY",
]
