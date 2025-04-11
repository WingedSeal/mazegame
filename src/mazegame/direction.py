from enum import Enum, auto


class Direction(Enum):
    LEFT = (-1, 0)
    RIGHT = (1, 0)
    UP = (0, -1)
    DOWN = (0, 1)
    HALT = (0, 0)

    def __str__(self) -> str:
        match self:
            case Direction.LEFT:
                return "Left"
            case Direction.RIGHT:
                return "Right"
            case Direction.UP:
                return "Up"
            case Direction.DOWN:
                return "Down"
            case Direction.HALT:
                return "Halt"
