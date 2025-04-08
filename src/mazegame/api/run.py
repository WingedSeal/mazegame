import threading
from typing import Callable

from ..game import Game
from ..map import Map
from .game_obj import get_game
from . import game_obj


def run(script: Callable[[], None], map: Map) -> None:
    game_obj.game = Game(map)

    def updated_script() -> None:
        get_game().control.pre_run()
        script()
        get_game().control.post_run()

    script_thread = threading.Thread(target=updated_script, daemon=True)
    script_thread.start()
    get_game().run()
