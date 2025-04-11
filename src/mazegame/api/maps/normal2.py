import random
from ...map import Exit, Map, Block, Player, Spike


map = [
    [Block(), Spike(), Block()],
    [Spike(), Player(), Spike()],
    [Block(), Spike(), Block()],
]

x, y = random.choice([(0, 1), (1, 0), (1, 2), (2, 1)])
map[y][x] = Exit()

NORMAL2 = Map(map)

# def script():
#     if get_tile(UP) == EXIT:
#         move(UP)
#     if get_tile(DOWN) == EXIT:
#         move(DOWN)
#     if get_tile(LEFT) == EXIT:
#         move(LEFT)
#     if get_tile(RIGHT) == EXIT:
#         move(RIGHT)
