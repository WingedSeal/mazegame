from mazegame.map import Map, Block, Player


TEST_MAP = Map(
    [
        [None, None, None, None, Block(), None, Block()],
        [None, None, None, None, Block(), None, Block()],
        [None, None, None, None, Player(), None, Player()],
    ]
)
