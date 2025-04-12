from ...map import Block, Exit, Map, Player, Spike


TUTORIAL5_1 = Map(
    [
        [Block(), Exit(), Block(), Block(), None],
        [Block(), None, Block(), Spike(), None],
        [Block(), Player(), Block(), Player(), None],
    ]
)

TUTORIAL5 = (
    [TUTORIAL5_1],
    "If you try moving a player into a wall, that player will not move!",
)

# def script():
#     move(RIGHT)
#     move(UP)
#     move(UP)
