from mazegame import *


def script():
    move(LEFT)
    print(get_tile())
    print(get_tile() == COLORED_FLOOR)
    print(get_color())
    print(get_color() == BLUE)
    move(LEFT)
    move(UP)
    move(LEFT)
    move(HALT)
    move(UP)


run(script, TEST_MAP)
