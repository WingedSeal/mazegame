from enum import Enum
from pygame import Color as _Color


class Color(Enum):
    RED = _Color(255, 0, 0)
    GREEN = _Color(0, 255, 0)
    BLUE = _Color(0, 0, 255)
