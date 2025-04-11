from mazegame import *


def script():
    while get_color(RIGHT) != PURPLE:
        move(UP)
    move(UP)
    move(RIGHT)


run(script, EXAMPLE2)
