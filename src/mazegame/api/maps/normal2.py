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
