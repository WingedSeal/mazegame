import random
from ...map import CustomMapType, Exit, Map, Block, Player, Spike


def _get_map():
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

    return ([Map(map) for map in maps], "The spike can spawn on any tile next to you.")


NORMAL2: CustomMapType = _get_map

# def script():
#     if get_tile(UP) == EXIT:
#         move(UP)
#     if get_tile(DOWN) == EXIT:
#         move(DOWN)
#     if get_tile(LEFT) == EXIT:
#         move(LEFT)
#     if get_tile(RIGHT) == EXIT:
#         move(RIGHT)
