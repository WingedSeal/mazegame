from mazegame import *


def script():
    for _ in range(5):
        wait()
    for _ in range(5):
        move(UP)
    for _ in range(5):
        move(DOWN)
    move(RIGHT)
    move(RIGHT)
    for _ in range(3):
        move(UP)


run(script, NORMAL4)
