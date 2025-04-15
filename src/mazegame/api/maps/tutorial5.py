from ...map import Block, CustomMapType, Exit, Map, Player, Spike


def _get_map():
    TUTORIAL5_1 = Map(
        [
            [Block(), Exit(), Block(), Block(), None],
            [Block(), None, Block(), Spike(), None],
            [Block(), Player(), Block(), Player(), None],
        ]
    )

    return (
        [TUTORIAL5_1],
        "If you try moving a player into a wall, that player will not move!",
    )


TUTORIAL5: CustomMapType = _get_map

# def script():
#     move(RIGHT)
#     move(UP)
#     move(UP)
