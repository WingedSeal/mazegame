import random

from ...color import Color
from ...map import ColoredFloor, Door, DoorFrame, Exit, Map, Block, Player, Spike, Lock


color1, color2, color3, color4 = Color.get_unique_colors(4)
NORMAL3_1 = Map(
    [
        [
            Exit(),
            Lock(color3),
            DoorFrame(Door(color3)),
            None,
            DoorFrame(Door(color4)),
            Lock(color4),
            Spike(),
        ],
        [Block(), Block(), Block(), ColoredFloor(color1), Block(), Block(), Block()],
        [Block(), Block(), Block(), None, Block(), Block(), Block()],
        [Block(), Block(), Block(), None, Block(), Block(), Block()],
        [Block(), Block(), Block(), ColoredFloor(color1), Block(), Block(), Block()],
        [Block(), Block(), Block(), Player(), Block(), Block(), Block()],
    ]
)

NORMAL3 = NORMAL3_1
