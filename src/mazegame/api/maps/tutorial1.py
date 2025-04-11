from ...map import Block, Exit, Map, Player

# fmt: off
TUTORIAL1 = Map(
    [
        [Block(), Exit(), Block()],
        [Block(), None, Block()],
        [Block(), None, Block()],
        [Block(), None, Block()],
        [Block(), Player(), Block()]
    ]
)
# fmt: on


# def script():
#     for _ in range(4):
#         move(UP)
