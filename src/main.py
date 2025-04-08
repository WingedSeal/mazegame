from mazegame.api.game_obj import get_game
from mazegame.api.run import run
from mazegame.map import TEST_MAP


def script():
    get_game().control._move(-1, 0)
    get_game().control._move(-1, 0)
    get_game().control._move(0, -1)
    get_game().control._move(-1, 0)
    get_game().control.halt()
    get_game().control._move(0, -1)


run(script, TEST_MAP)
