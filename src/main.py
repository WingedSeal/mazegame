from mazegame import *


def script():
    move(LEFT)
    print(get_tile())
    print(get_color())
    move(LEFT)
    move(UP)
    move(LEFT)
    move(HALT)
    move(UP)


run(script, TEST_MAP)
