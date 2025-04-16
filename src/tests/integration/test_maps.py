import sys
from typing import cast


sys.path.append("./src")  # noqa

import os
import unittest
import inspect
from mazegame import *
from mazegame.map import CustomMapType  # noqa
from mazegame.api.run import _test_run
from mazegame.api import maps as _maps


def empty_script():
    pass


class TestMaps(unittest.TestCase):
    def test_all_maps(self):
        all_maps = inspect.getmembers(_maps, inspect.isfunction)
        for map_name, map in all_maps:
            try:
                map = cast(CustomMapType, map)
                _test_run(empty_script, map()[0], exit_on_tick=1)
            except:
                self.fail(f"{map_name} failed to start.")


if __name__ == "__main__":
    unittest.main()
