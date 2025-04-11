from ...color import Color
from ...direction import Direction
from ...map import Block, Door, Enemy, Exit, Key, Map, Player

color = Color.get_unique_colors(1)[0]

TUTORIAL4 = Map(
    [
        [Block(), Exit(), Block()],
        [Block(), Door(color), Block()],
        [Block(), Player(), Block()],
        [Block(), Key(color), Block()],
    ]
)

# def script():
#     move(DOWN)
#     for _ in range(3):
#         move(UP)
