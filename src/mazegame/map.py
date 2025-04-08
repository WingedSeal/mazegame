from abc import ABC, abstractmethod
from typing import Type, TypeVar

import pygame

from .direction import Direction
from .color import Color


def _lerp(a: tuple[float, float], b: tuple[float, float], t: float) -> tuple[int, int]:
    return (
        int((1 - t) * a[0] + t * b[0]),
        int((1 - t) * a[1] + t * b[1]),
    )


def _dash_lerp(
    a: tuple[float, float], b: tuple[float, float], t: float
) -> tuple[int, int]:
    return _lerp(a, b, 1 - (1 - t) ** 4)


class Tile(ABC, pygame.sprite.Sprite):
    surf: pygame.Surface
    tile_size = 0
    rect: pygame.Rect
    pos: tuple[int, int] = (0, 0)
    old_pos: tuple[int, int] = (0, 0)

    @abstractmethod
    def init(self, pos: tuple[int, int], tile_size: int) -> None:
        pass

    def _pos_to_pixel(self, pos: tuple[int, int]) -> tuple[int, int]:
        return self.tile_size * pos[0], self.tile_size * pos[1]

    def animate(self, t: float):
        """
        Animate moving tile, default to dash lerp.

        :param start: start position
        :param end: end position
        :param t: time range between 0 and 1
        """
        pixel_pos = _dash_lerp(
            self._pos_to_pixel(self.old_pos), self._pos_to_pixel(self.pos), t
        )
        self.rect.topleft = pixel_pos


T = TypeVar("T", bound=Tile)


class TouchableTile(Tile):
    @abstractmethod
    def interact(self, other_tile: Tile) -> None:
        pass


class Block(Tile):
    def init(self, pos: tuple[int, int], tile_size: int) -> None:
        self.tile_size = tile_size
        self.pos = pos
        self.surf = pygame.Surface((tile_size, tile_size))
        self.surf.fill((255, 255, 0))
        self.rect = self.surf.get_rect()
        self.rect.topleft = self._pos_to_pixel(pos)


class ColorFloor(Tile):
    def __init__(self, color: Color) -> None:
        self.color = color
        super().__init__()


class Player(Tile):
    def init(self, pos: tuple[int, int], tile_size: int) -> None:
        self.tile_size = tile_size
        self.pos = pos
        self.surf = pygame.Surface((tile_size, tile_size))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect()
        self.rect.topleft = self._pos_to_pixel(pos)


class Door(Tile):
    def __init__(self, color: Color) -> None:
        self.color = color
        super().__init__()


class Key(TouchableTile):
    def __init__(self, color: Color) -> None:
        self.color = color
        super().__init__()


class Spike(TouchableTile):
    pass


class Enemy(TouchableTile):
    def __init__(self, path: list[Direction], chance_to_move: float = 1.0) -> None:
        self.index = 0
        self.path = path
        self.chance_to_move = chance_to_move
        super().__init__()

    def init(self, pos: tuple[int, int], tile_size: int) -> None:
        self.tile_size = tile_size
        self.pos = pos
        self.surf = pygame.Surface((tile_size, tile_size))
        self.surf.fill((255, 0, 255))
        self.rect = self.surf.get_rect()
        self.rect.topleft = self._pos_to_pixel(pos)

    def interact(self, other_tile: Tile) -> None:
        raise NotImplementedError("YOU DIED")


class Map:
    def __init__(self, map: list[list[Tile | None]]) -> None:
        self.map = map
        self.height = len(map)
        self.width = len(map[0]) if map else 0

    def get_positions(self, cls: Type[Tile]) -> list[tuple[int, int]]:
        """
        Find 1 or more positions of any tile type

        :return: tile position(s)
        """
        positions: list[tuple[int, int]] = []
        for y, row in enumerate(self.map):
            for x, tile in enumerate(row):
                if isinstance(tile, cls):
                    positions.append((x, y))
        return positions

    def get_tiles(self, cls: Type[T]) -> list[T]:
        """
        Find 1 or more tiles

        :return: tiles
        """
        tiles: list[T] = []
        for row in self.map:
            for tile in row:
                if isinstance(tile, cls):
                    tiles.append(tile)
        return tiles
