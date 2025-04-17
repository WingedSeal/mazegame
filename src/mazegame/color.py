from enum import Enum
import random
from pygame import Color as _Color


class Color(Enum):
    RED = _Color(255, 50, 50)
    ORANGE = _Color(255, 140, 0)
    YELLOW = _Color(255, 230, 50)
    GREEN = _Color(0, 200, 0)
    LIGHT_BLUE = _Color(100, 180, 255)
    BLUE = _Color(0, 100, 255)
    PURPLE = _Color(180, 100, 220)

    @classmethod
    def get_unique_colors(
        cls, count: int | None, exceptions: list["Color"] = []
    ) -> list["Color"]:
        """
        Randomize {count} colors from all possible colors. All of them are unique

        :param count: How many colors to randomize, or as many as possible if set to `None`
        """
        all_colors = [x for x in list(cls) if x not in exceptions]
        if count is None:
            count = len(all_colors)
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
            case Color.LIGHT_BLUE:
                return "Light Blue"
            case Color.BLUE:
                return "Blue"
            case Color.PURPLE:
                return "Purple"
