from abc import ABC

from .direction import Direction
from .color import Color


class Tile(ABC):
    pass


class Block(Tile):
    pass


BLOCK = Block()


class ColorFloor(Tile):
    def __init__(self, color: Color) -> None:
        self.color = color
        super().__init__()


class Player(Tile):
    pass


PLAYER = Player()


class Door(Tile):
    def __init__(self, color: Color) -> None:
        self.color = color
        super().__init__()


class Key(Tile):
    def __init__(self, color: Color) -> None:
        self.color = color
        super().__init__()


class Spike(Tile):
    pass


SPIKE = Spike()


class Enemy(Tile):
    def __init__(self, path: list[Direction]) -> None:
        self.path = path
        super().__init__()


class Map:
    def __init__(self, map: list[list[Tile | None]]) -> None:
        self.width = len(map)
        self.height = len(map[0]) if map else 0


TEST_MAP = Map([[None, None, BLOCK], [None, None, BLOCK], [None, None, PLAYER]])
