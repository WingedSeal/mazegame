from mazegame import *


def script():
    move(LEFT)
    move(LEFT)
    move(UP)
    print(get_tile(UP, 1))
    move(LEFT)
    move(HALT)
    move(UP)


run(script, TEST_MAP)
