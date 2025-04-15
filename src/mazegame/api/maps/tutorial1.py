from ...map import Block, CustomMapType, Exit, Map, Player


def _get_map():
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
    return ([TUTORIAL1_1], "Use 'move(UP)' to reach the exit!")


TUTORIAL1: CustomMapType = _get_map

# def script():
#     for _ in range(4):
#         move(UP)
