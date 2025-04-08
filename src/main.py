from mazegame import *


def script():
    move(LEFT)
    move(LEFT)
    move(UP)
    move(LEFT)
    move(HALT)
    move(UP)


run(script, TEST_MAP)
