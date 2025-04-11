from mazegame import *


def script():
    move(UP)
    color = get_color()
    for _ in range(3):
        move(UP)
    is_color_match = get_color() == color
    move(UP)
    for _ in range(3):
        if is_color_match:
            move(LEFT)
        else:
            move(RIGHT)


run(script, NORMAL3)
