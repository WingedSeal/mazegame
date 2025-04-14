from mazegame import *


def script():
    move(RIGHT)
    move(DOWN)
    move(DOWN)
    for _ in range(4):
        move(LEFT)
    for _ in range(4):
        move(UP)
    for _ in range(4):
        move(RIGHT)
    move(UP)
    move(RIGHT)
    move(UP)
    move(LEFT)
    move(DOWN)
    for _ in range(3):
        move(LEFT)
    move(UP)
    move(UP)


run(script, PRACTICE1)
# preview(PRACTICE1)
