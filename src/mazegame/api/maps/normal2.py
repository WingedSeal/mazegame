import random
from ...map import Exit, Map, Block, Player, Spike


maps = [
    [
        [Block(), Spike(), Block()],
        [Spike(), Player(), Spike()],
        [Block(), Spike(), Block()],
    ]
    for _ in range(4)
]

for i, (x, y) in enumerate(((0, 1), (1, 0), (1, 2), (2, 1))):
    maps[i][y][x] = Exit()

NORMAL2 = ([Map(map) for map in maps], "NORMAL2")

# def script():
#     if get_tile(UP) == EXIT:
#         move(UP)
#     if get_tile(DOWN) == EXIT:
#         move(DOWN)
#     if get_tile(LEFT) == EXIT:
#         move(LEFT)
#     if get_tile(RIGHT) == EXIT:
#         move(RIGHT)
