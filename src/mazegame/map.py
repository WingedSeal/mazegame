from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Type, TypeVar

import pygame

if TYPE_CHECKING:
    from .game import Game

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


class GetColor(ABC):
    @abstractmethod
    def get_color(self) -> Color:
        pass


class Tile(ABC, pygame.sprite.Sprite):
    surf: pygame.Surface
    tile_size = 0
    rect: pygame.Rect
    pos: tuple[int, int] = (0, 0)
    old_pos: tuple[int, int] = (0, 0)
    tile_under: "Tile | None" = None

    @abstractmethod
    def init(self, pos: tuple[int, int], tile_size: int) -> None:
        pass

    def _pos_to_pixel(
        self, pos: tuple[int, int], padding: tuple[int, int] = (0, 0)
    ) -> tuple[int, int]:
        return (
            self.tile_size * pos[0] + padding[0],
            self.tile_size * pos[1] + padding[1],
        )

    def get_top_left(self, pos: tuple[int, int]) -> tuple[int, int]:
        return self._pos_to_pixel(pos)

    def animate(self, t: float):
        """
        Animate moving tile, default to dash lerp.

        :param start: start position
        :param end: end position
        :param t: time range between 0 and 1
        """
        pixel_pos = _dash_lerp(
            self.get_top_left(self.old_pos), self.get_top_left(self.pos), t
        )
        self.rect.topleft = pixel_pos

    def __eq__(self, value: object) -> bool:
        if type(self) == type(value):
            return True
        if isinstance(value, str):
            if self.__class__.__name__ == value:
                return True
        return False

    def __str__(self) -> str:
        return f"{self.__class__.__name__} at {self.pos}"

    # def __repr__(self) -> str:
    #     return str(self)


T = TypeVar("T", bound=Tile)


class TouchableTile(Tile):
    can_be_under = True

    @abstractmethod
    def interact(self, other_tile: Tile, game: "Game") -> None:
        pass


class Block(Tile):
    def init(self, pos: tuple[int, int], tile_size: int) -> None:
        self.tile_size = tile_size
        self.pos = pos
        if not hasattr(type(self), "surf"):
            type(self).surf = pygame.Surface((tile_size, tile_size))
            type(self).surf.fill((255, 255, 0))
        self.rect = self.surf.get_rect()


class ColoredFloor(TouchableTile, GetColor):
    surfs: dict[Color, pygame.Surface] = {}

    def __init__(self, color: Color) -> None:
        self.color = color
        super().__init__()

    def init(self, pos: tuple[int, int], tile_size: int) -> None:
        self.tile_size = tile_size
        self.pos = pos
        if self.color.value in self.surfs:
            self.surf = self.surfs[self.color]
        else:
            self.surf = pygame.Surface((tile_size, tile_size))
            self.surf.fill(self.color.value)
            self.surfs[self.color] = self.surf

        self.rect = self.surf.get_rect()

    def interact(self, other_tile: Tile, game: "Game") -> None:
        pass

    def get_color(self) -> Color:
        return self.color

    def __str__(self) -> str:
        return f"{self.color} {self.__class__.__name__} at {self.pos}"


class ColoredBlock(Tile, GetColor):
    surfs: dict[Color, pygame.Surface] = {}

    def __init__(self, color: Color) -> None:
        self.color = color
        super().__init__()

    def init(self, pos: tuple[int, int], tile_size: int) -> None:
        self.tile_size = tile_size
        self.pos = pos
        if self.color.value in self.surfs:
            self.surf = self.surfs[self.color]
        else:
            self.surf = pygame.Surface((tile_size, tile_size))
            self.surf.fill(self.color.value)
            self.surfs[self.color] = self.surf

        self.rect = self.surf.get_rect()

    def get_color(self) -> Color:
        return self.color

    def __str__(self) -> str:
        return f"{self.color} {self.__class__.__name__} at {self.pos}"


class Player(TouchableTile):
    index: int

    def init(self, pos: tuple[int, int], tile_size: int) -> None:
        self.tile_size = tile_size
        self.pos = pos
        if not hasattr(type(self), "surf"):
            type(self).surf = pygame.Surface((tile_size * 0.9, tile_size * 0.9))
            type(self).surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect()

    def get_top_left(self, pos: tuple[int, int]) -> tuple[int, int]:
        return self._pos_to_pixel(
            pos, padding=(int(self.tile_size * 0.05), int(self.tile_size * 0.05))
        )

    def interact(self, other_tile: Tile, game: "Game") -> None:
        if isinstance(other_tile, Enemy):
            raise NotImplementedError("You died, enemy ran into you")


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


class Exit(TouchableTile):
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
        if not hasattr(type(self), "surf"):
            type(self).surf = pygame.Surface((tile_size, tile_size))
            type(self).surf.fill((255, 0, 255))
        self.rect = self.surf.get_rect()

    def interact(self, other_tile: Tile, game: "Game") -> None:
        if not isinstance(other_tile, Player):
            return

        game.game_over("YOU RAN INTO ENEMY", "NOPE")


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


# TODO: MAKE SURE ALL INSTANCES SHARE A SURFACE, split init into per class (tile_size) and per instance
