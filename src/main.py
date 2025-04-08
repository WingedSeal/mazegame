import threading
from mazegame.control import Control
from mazegame.game import Game
from mazegame.map import TEST_MAP

game = Game(TEST_MAP)
control = game.control
t2 = threading.Thread(target=control.test_run, daemon=True)
t2.start()
game.run()
