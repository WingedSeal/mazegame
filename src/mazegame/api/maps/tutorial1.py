from ...map import Block, Exit, Map, Player

# fmt: off
TUTORIAL1_1 = Map(
    [
        [Block(), Exit(), Block()],
        [Block(), None, Block()],
        [Block(), None, Block()],
        [Block(), None, Block()],
        [Block(), Player(), Block()]
    ]
)
# fmt: on

TUTORIAL1 = ([TUTORIAL1_1], "TUTORIAL1")

# def script():
#     for _ in range(4):
#         move(UP)
