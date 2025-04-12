from mazegame.map import Block, Enemy, Map
from mazegame.preview import Preview
from mazegame import *


def script():
    pass


# run(script, TUTORIAL2)


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
