from ...direction import Direction
from ...map import Block, Enemy, Exit, Map, Player

TUTORIAL3 = Map(
    [
        [Block(), Block(), Exit(), Block()],
        [
            None,
            None,
            Enemy([Direction.LEFT] * 2 + [Direction.RIGHT] * 2, chance_to_move=0.5),
            Block(),
        ],
        [Block(), Block(), Player(), Block()],
    ]
)
