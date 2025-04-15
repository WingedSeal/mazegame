from ...direction import Direction
from ...map import Block, CustomMapType, Enemy, Exit, Map, Player


def _get_map():
    TUTORIAL3_1 = Map(
        [
            [Block(), Block(), Exit(), Block()],
            [
                None,
                None,
                Enemy(
                    [Direction.LEFT] * 2 + [Direction.RIGHT] * 2,
                    chance_to_move=0.5,
                    boss=True,
                ),
                Block(),
            ],
            [Block(), Block(), Player(), Block()],
        ]
    )
    return ([TUTORIAL3_1], "Wait for enemy to move out of the way before moving!")


TUTORIAL3: CustomMapType = _get_map

# def script():
#     while get_tile(UP) == ENEMY:
#         wait()
#     move(UP)
#     move(UP)
