from mazegame import *


def script():
    move(UP)
    move(UP)
    move(UP)
    move(UP)
    while get_tile(UP) != ENEMY:
        move(HALT)
    while get_tile(UP) == ENEMY:
        move(HALT)
    count = 0
    while count < 5:
        if get_tile(UP) == ENEMY:
            move(HALT)
        else:
            move(UP)
            count += 1
    move(RIGHT)
    while get_tile(LEFT) != ENEMY:
        move(HALT)
    while get_tile(LEFT) == ENEMY:
        move(HALT)
    move(LEFT)
    for _ in range(6):
        move(UP)
    move(RIGHT)


run(script, HARD1)
