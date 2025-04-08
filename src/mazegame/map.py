from abc import ABC, abstractmethod

import pygame
from pygame.math import Vector2

from .direction import Direction
from .color import Color


def _lerp(a: tuple[float, float], b: tuple[float, float], t: float) -> tuple[int, int]:
    return int((1 - t) * a[0]) + int(t * b[0]), int((1 - t) * a[1]) + int(t * b[1])


def _pos_to_pixel(pos: tuple[int, int], tile_size: int) -> tuple[int, int]:
    return tile_size * pos[0], tile_size * pos[1]


class Tile(ABC, pygame.sprite.Sprite):
    surf: pygame.Surface
    tile_size = 0
    rect: pygame.Rect
    pos: tuple[int, int] = (0, 0)
    old_pos: tuple[int, int] = (0, 0)

    @abstractmethod
    def init(self, pos: tuple[int, int], tile_size: int) -> None:
        pass

    def animate(self, t: float):
        """
        Animate moving tile, default lerp.

        :param start: start position
        :param end: end position
        :param t: time range between 0 and 1
        """
        print()
        pos = _lerp(self.old_pos, self.pos, t)
        self.rect.topleft = (self.tile_size * pos[0], self.tile_size * pos[1])


class Block(Tile):
    def init(self, pos: tuple[int, int], tile_size: int) -> None:
        self.tile_size = tile_size
        self.pos = pos
        self.surf = pygame.Surface((tile_size, tile_size))
        self.surf.fill((255, 255, 0))
        self.rect = self.surf.get_rect()
        self.rect.topleft = (tile_size * pos[0], tile_size * pos[1])


class ColorFloor(Tile):
    def __init__(self, color: Color) -> None:
        self.color = color
        super().__init__()


class Player(Tile):
    def init(self, pos: tuple[int, int], tile_size: int) -> None:
        self.pos = pos
        self.surf = pygame.Surface((tile_size, tile_size))
        self.surf.fill((255, 255, 0))
        self.rect = self.surf.get_rect()
        self.rect.topleft = (tile_size * pos[0], tile_size * pos[1])


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


class Enemy(Tile):
    def __init__(self, path: list[Direction]) -> None:
        self.path = path
        super().__init__()


class Map:
    def __init__(self, map: list[list[Tile | None]]) -> None:
        self.map = map
        self.width = len(map)
        self.height = len(map[0]) if map else 0


TEST_MAP = Map([[None, None, Block()], [None, None, Block()], [None, None, Player()]])
