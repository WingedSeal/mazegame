from mazegame import *


def script():
    move(RIGHT)
    move(DOWN)
    move(LEFT)
    move(UP)
    for _ in range(3):
        move(LEFT)
    move(UP)
    move(RIGHT)
    for _ in range(3):
        move(DOWN)
    move(LEFT)
    for _ in range(2):
        move(UP)
    for _ in range(5):
        move(RIGHT)


run(script, EXAMPLE1)
