from enum import Enum
import random
from pygame import Color as _Color


class Color(Enum):
    RED = _Color(255, 0, 0)
    ORANGE = _Color(255, 165, 0)
    YELLOW = _Color(255, 255, 0)
    GREEN = _Color(0, 255, 0)
    BLUE = _Color(0, 0, 255)
    DEEP_BLUE = _Color(75, 0, 130)
    PURPLE = _Color(238, 130, 238)

    @classmethod
    def get_unique_colors(cls, count: int) -> list["Color"]:
        """
        Randomize {count} colors from all possible colors. All of them are unique

        :param count: How many colors to randomize
        """
        all_colors = list(cls)
        if count > len(all_colors):
            raise ValueError(
                f"Cannot select {count} unique colors from {len(all_colors)} available colors."
            )
        selected_colors = random.sample(all_colors, count)

        return selected_colors

    def __str__(self) -> str:
        match self:
            case Color.RED:
                return "Red"
            case Color.ORANGE:
                return "Orange"
            case Color.YELLOW:
                return "Yellow"
            case Color.GREEN:
                return "Green"
            case Color.BLUE:
                return "Blue"
            case Color.DEEP_BLUE:
                return "Deep Blue"
            case Color.PURPLE:
                return "Purple"
