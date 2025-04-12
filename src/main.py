from mazegame.map import Block, Enemy, Map
from mazegame.preview import Preview
from mazegame import *


def script():
    return


Preview(
    [
        Map(
            [
                [Block(), Block(), Block()],
                [Block(), None, None],
                [Block(), None, Enemy(path=[UP, LEFT, UP, RIGHT, DOWN])],
            ]
        ),
        Map(
            [
                [Block(), None, Block()],
                [Block(), None, None],
                [Block(), None, Enemy(path=[UP, LEFT, UP, RIGHT, DOWN])],
            ]
        ),
    ]
).run()

# run(script, NORMAL4)
