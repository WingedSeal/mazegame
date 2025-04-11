from abc import ABC, abstractmethod
import random
from typing import TYPE_CHECKING, Any, Type, TypeVar, override


import pygame


if TYPE_CHECKING:
    from .game import Game

from .direction import Direction
from .color import Color

SurfsType = dict[type["Tile"] | tuple[type["HasColor"], Color], pygame.Surface]

_BLOCK_EDGE_COLOR = pygame.Color(215, 220, 225)
_BLOCK_COLOR = pygame.Color(195, 200, 205)
_ENEMY_COLOR = pygame.Color(220, 20, 60)
_SPIKE_COLOR = pygame.Color(128, 0, 128)
_PLAYER_COLOR = pygame.Color(102, 255, 255)
_EXIT_OUTER_COLOR = pygame.Color(0, 150, 0)
_EXIT_INNER_COLOR = pygame.Color(102, 255, 102)
_DOOR_COLOR = pygame.Color(139, 69, 19)


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
    tile_under: "Tile | None" = None
    _auto_remove: bool = False

    @abstractmethod
    def init(
        self,
        pos: tuple[int, int],
        tile_size: int,
        surfs: SurfsType,
    ) -> None:
        pass

    def _pos_to_pixel(
        self, pos: tuple[int, int], padding: tuple[int, int] = (0, 0)
    ) -> tuple[int, int]:
        return (
            self.tile_size * pos[0] + padding[0],
            self.tile_size * pos[1] + padding[1],
        )

    def drop(self) -> None:
        pass

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


class HasColor:
    @abstractmethod
    def get_color(self) -> Color:
        pass


class TouchableTile(Tile):
    @abstractmethod
    def interacted_with(self, other_tile: Tile, game: "Game") -> None:
        pass


class Block(Tile):
    def init(
        self,
        pos: tuple[int, int],
        tile_size: int,
        surfs: SurfsType,
    ) -> None:
        self.tile_size = tile_size
        self.pos = pos
        if type(self) not in surfs:
            self.surf = pygame.Surface((tile_size, tile_size))
            self.surf.fill(_BLOCK_COLOR)
            self.surf.fill(_BLOCK_EDGE_COLOR, (0, 0, tile_size, tile_size * 0.1))
            self.surf.fill(
                _BLOCK_EDGE_COLOR, (0, tile_size * 0.9, tile_size, tile_size * 0.1)
            )
            self.surf.fill(_BLOCK_EDGE_COLOR, (0, 0, tile_size * 0.1, tile_size))
            self.surf.fill(
                _BLOCK_EDGE_COLOR, (tile_size * 0.9, 0, tile_size * 0.1, tile_size)
            )
            surfs[type(self)] = self.surf
        else:
            self.surf = surfs[type(self)]
        self.rect = self.surf.get_rect()


class ColoredFloor(TouchableTile, HasColor):
    surfs: dict[Color, pygame.Surface] = {}

    def __init__(self, color: Color) -> None:
        self.color = color
        super().__init__()

    def init(
        self,
        pos: tuple[int, int],
        tile_size: int,
        surfs: SurfsType,
    ) -> None:
        self.tile_size = tile_size
        self.pos = pos
        if (type(self), self.color) not in surfs:
            self.surf = pygame.Surface((tile_size, tile_size))
            self.surf.fill(self.color.value)
            surfs[type(self), self.color] = self.surf
        else:
            self.surf = surfs[type(self), self.color]
        self.rect = self.surf.get_rect()

    def interacted_with(self, other_tile: Tile, game: "Game") -> None:
        pass

    def get_color(self) -> Color:
        return self.color

    def __str__(self) -> str:
        return f"{self.color} {self.__class__.__name__} at {self.pos}"


class ColoredBlock(Tile, HasColor):
    surfs: dict[Color, pygame.Surface] = {}

    def __init__(self, color: Color) -> None:
        self.color = color
        super().__init__()

    def init(
        self,
        pos: tuple[int, int],
        tile_size: int,
        surfs: SurfsType,
    ) -> None:
        self.tile_size = tile_size
        self.pos = pos
        if (type(self), self.color) not in surfs:
            self.surf = pygame.Surface((tile_size, tile_size))
            self.surf.fill(self.color.value)
            self.surf.fill(_BLOCK_EDGE_COLOR, (0, 0, tile_size, tile_size * 0.1))
            self.surf.fill(
                _BLOCK_EDGE_COLOR, (0, tile_size * 0.9, tile_size, tile_size * 0.1)
            )
            self.surf.fill(_BLOCK_EDGE_COLOR, (0, 0, tile_size * 0.1, tile_size))
            self.surf.fill(
                _BLOCK_EDGE_COLOR, (tile_size * 0.9, 0, tile_size * 0.1, tile_size)
            )

            surfs[type(self), self.color] = self.surf
        else:
            self.surf = surfs[type(self), self.color]
        self.rect = self.surf.get_rect()

    def get_color(self) -> Color:
        return self.color

    def __str__(self) -> str:
        return f"{self.color} {self.__class__.__name__} at {self.pos}"


class Player(TouchableTile):
    index: int

    def init(
        self,
        pos: tuple[int, int],
        tile_size: int,
        surfs: SurfsType,
    ) -> None:
        self.tile_size = tile_size
        self.pos = pos
        if type(self) not in surfs:
            self.surf = pygame.Surface((tile_size, tile_size), pygame.SRCALPHA)
            pygame.draw.circle(
                self.surf,
                _PLAYER_COLOR,
                (tile_size // 2, tile_size // 2),
                0.9 * tile_size // 2,
            )
            surfs[type(self)] = self.surf
        else:
            self.surf = surfs[type(self)]
        self.rect = self.surf.get_rect()

    def interacted_with(self, other_tile: Tile, game: "Game") -> None:
        if not isinstance(other_tile, Enemy):
            return
        game.game_over(
            "Enemy ran into you.",
            random.choice(
                [
                    "That plan did not go well",
                    "Consider not dying, that's not a great plan",
                    '"Avoid collision" was a suggestion, apparently.',
                    "Dying isn't good for your health.",
                    "You have to be alive to win by the way.",
                ]
            ),
        )


_HIDEN_KEY_DO_NO_INSTANCIATE = object()


class Door(Tile, HasColor):
    surfs: dict[Color, pygame.Surface] = {}

    def __init__(self, color: Color, *, open: bool = False) -> None:
        self.color = color
        self.tile_under = DoorFrame(self, _HIDEN_KEY_DO_NO_INSTANCIATE)
        if open:
            self._auto_remove = True
        super().__init__()

    def init(
        self,
        pos: tuple[int, int],
        tile_size: int,
        surfs: SurfsType,
    ) -> None:
        self.tile_size = tile_size
        self.pos = pos
        if type(self) not in surfs:
            self.surf = pygame.Surface((tile_size, tile_size), pygame.SRCALPHA)
            self.surf.fill(
                _DOOR_COLOR,
                (tile_size * 0.1, tile_size * 0.2, tile_size * 0.375, tile_size * 0.6),
            )
            self.surf.fill(
                _DOOR_COLOR,
                (
                    tile_size * 0.525,
                    tile_size * 0.2,
                    tile_size * 0.375,
                    tile_size * 0.6,
                ),
            )
            surfs[type(self)] = self.surf
        else:
            self.surf = surfs[type(self)]
        self.rect = self.surf.get_rect()

    def get_color(self) -> Color:
        return self.color

    def __str__(self) -> str:
        return f"{self.color} {self.__class__.__name__} at {self.pos}"


class DoorFrame(TouchableTile, HasColor):
    surfs: dict[Color, pygame.Surface] = {}

    def __init__(self, door: Door, _hiden_key: object) -> None:
        if _hiden_key is not _HIDEN_KEY_DO_NO_INSTANCIATE:
            raise Exception("Do not construct DoorFrame object manually.")
        self.color = door.color
        self.door = door

    def init(
        self,
        pos: tuple[int, int],
        tile_size: int,
        surfs: SurfsType,
    ) -> None:
        self.tile_size = tile_size
        self.pos = pos
        if (type(self), self.color) not in surfs:
            self.surf = pygame.Surface((tile_size, tile_size), pygame.SRCALPHA)
            self.surf.fill(
                self.color.value,
                (0, 0, tile_size * 0.1, tile_size),
            )
            self.surf.fill(
                self.color.value,
                (tile_size * 0.9, 0, tile_size * 0.1, tile_size),
            )
            self.surf.fill(
                _DOOR_COLOR,
                (tile_size * 0.1, tile_size * 0.2, tile_size * 0.025, tile_size * 0.6),
            )
            self.surf.fill(
                _DOOR_COLOR,
                (
                    tile_size * 0.875,
                    tile_size * 0.2,
                    tile_size * 0.025,
                    tile_size * 0.6,
                ),
            )
            surfs[type(self), self.color] = self.surf
        else:
            self.surf = surfs[type(self), self.color]
        self.rect = self.surf.get_rect()

    def interacted_with(self, other_tile: Tile, game: "Game") -> None:
        pass

    def get_color(self) -> Color:
        return self.color

    def __str__(self) -> str:
        return f"{self.color} {self.__class__.__name__} at {self.pos}"


class Key(TouchableTile, HasColor):
    surfs: dict[Color, pygame.Surface] = {}

    def __init__(self, color: Color) -> None:
        self.color = color
        super().__init__()

    def interacted_with(self, other_tile: Tile, game: "Game") -> None:
        if not isinstance(other_tile, Player):
            return
        other_tile.tile_under = None
        for y, row in enumerate(game.map.map):
            for x, tile in enumerate(row):
                if isinstance(tile, Door) and tile.color == self.color:
                    game.map.map[y][x] = tile.tile_under

    def init(
        self,
        pos: tuple[int, int],
        tile_size: int,
        surfs: SurfsType,
    ) -> None:
        self.tile_size = tile_size
        self.pos = pos
        if (type(self), self.color) not in surfs:
            self.surf = pygame.Surface((tile_size, tile_size), pygame.SRCALPHA)
            pygame.draw.circle(
                self.surf,
                self.color.value,
                (tile_size // 2, int(0.64 * tile_size)),
                int(0.06 * tile_size),
            )
            points: list[tuple[int, int]] = [
                (int(0.475 * tile_size), int(0.64 * tile_size)),
                (int(0.475 * tile_size), int(0.3 * tile_size)),
                (int(0.525 * tile_size), int(0.3 * tile_size)),
                (int(0.525 * tile_size), int(0.35 * tile_size)),
                (int(0.625 * tile_size), int(0.35 * tile_size)),
                (int(0.625 * tile_size), int(0.4 * tile_size)),
                (int(0.525 * tile_size), int(0.4 * tile_size)),
                (int(0.525 * tile_size), int(0.425 * tile_size)),
                (int(0.625 * tile_size), int(0.425 * tile_size)),
                (int(0.625 * tile_size), int(0.475 * tile_size)),
                (int(0.525 * tile_size), int(0.475 * tile_size)),
                (int(0.525 * tile_size), int(0.64 * tile_size)),
            ]

            pygame.draw.polygon(self.surf, self.color.value, points)

            surfs[type(self), self.color] = self.surf
        else:
            self.surf = surfs[type(self), self.color]
        self.rect = self.surf.get_rect()

    def get_color(self) -> Color:
        return self.color

    def __str__(self) -> str:
        return f"{self.color} {self.__class__.__name__} at {self.pos}"


class Lock(TouchableTile, HasColor):
    surfs: dict[Color, pygame.Surface] = {}

    def __init__(self, color: Color) -> None:
        self.color = color
        super().__init__()

    def interacted_with(self, other_tile: Tile, game: "Game") -> None:
        if not isinstance(other_tile, Player):
            return
        other_tile.tile_under = None
        for y, row in enumerate(game.map.map):
            for x, tile in enumerate(row):
                if isinstance(tile, DoorFrame) and tile.color == self.color:
                    game.map.map[y][x] = tile.door

    def init(
        self,
        pos: tuple[int, int],
        tile_size: int,
        surfs: SurfsType,
    ) -> None:
        self.tile_size = tile_size
        self.pos = pos
        if (type(self), self.color) not in surfs:
            self.surf = pygame.Surface((tile_size, tile_size), pygame.SRCALPHA)
            pygame.draw.circle(
                self.surf,
                self.color.value,
                (tile_size // 2, int(0.4 * tile_size)),
                int(0.1 * tile_size),
            )
            pygame.draw.circle(
                self.surf,
                (0, 0, 0, 0),
                (tile_size // 2, int(0.4 * tile_size)),
                int(0.075 * tile_size),
            )
            self.surf.fill(
                (0, 0, 0, 0),
                (
                    tile_size * 0.4,
                    tile_size * 0.4,
                    tile_size * 0.2,
                    tile_size * 0.1,
                ),
            )
            self.surf.fill(
                self.color.value,
                (
                    tile_size * 0.4,
                    tile_size * 0.4,
                    tile_size * 0.025,
                    tile_size * 0.1,
                ),
            )
            self.surf.fill(
                self.color.value,
                (
                    tile_size * 0.575,
                    tile_size * 0.4,
                    tile_size * 0.025,
                    tile_size * 0.1,
                ),
            )
            self.surf.fill(
                self.color.value,
                (
                    tile_size * 0.35,
                    tile_size * 0.5,
                    tile_size * 0.3,
                    tile_size * 0.15,
                ),
            )

            surfs[type(self), self.color] = self.surf
        else:
            self.surf = surfs[type(self), self.color]
        self.rect = self.surf.get_rect()

    def get_color(self) -> Color:
        return self.color

    def __str__(self) -> str:
        return f"{self.color} {self.__class__.__name__} at {self.pos}"


class Spike(TouchableTile):
    def init(
        self,
        pos: tuple[int, int],
        tile_size: int,
        surfs: SurfsType,
    ) -> None:
        self.tile_size = tile_size
        self.pos = pos
        if type(self) not in surfs:
            self.surf = pygame.Surface((tile_size, tile_size), pygame.SRCALPHA)
            points: list[tuple[int, int]] = [
                (0, tile_size),
                (tile_size * 1 // 6, 0),
                (tile_size * 2 // 6, int(tile_size * 0.9)),
                (tile_size * 3 // 6, 0),
                (tile_size * 4 // 6, int(tile_size * 0.9)),
                (tile_size * 5 // 6, 0),
                (tile_size, tile_size),
            ]

            pygame.draw.polygon(self.surf, _SPIKE_COLOR, points)
            surfs[type(self)] = self.surf
        else:
            self.surf = surfs[type(self)]
        self.rect = self.surf.get_rect()

    def interacted_with(self, other_tile: Tile, game: "Game") -> None:
        if not isinstance(other_tile, Player):
            return

        game.game_over(
            "You ran into a spike.",
            random.choice(
                [
                    "Did that spike not lsook dangerous.",
                    "It wasn't even moving.",
                    "Dying isn't good for your health.",
                    "Consider not doing that.",
                    "That's the spike!",
                ]
            ),
        )


class Exit(TouchableTile):
    def init(
        self,
        pos: tuple[int, int],
        tile_size: int,
        surfs: SurfsType,
    ) -> None:
        self.tile_size = tile_size
        self.pos = pos
        if type(self) not in surfs:
            self.surf = pygame.Surface((tile_size, tile_size), pygame.SRCALPHA)
            self.surf.fill(_EXIT_OUTER_COLOR)
            pygame.draw.circle(
                self.surf,
                _EXIT_INNER_COLOR,
                (tile_size // 2, tile_size // 2),
                0.9 * tile_size // 2,
            )
            surfs[type(self)] = self.surf
        else:
            self.surf = surfs[type(self)]
        self.rect = self.surf.get_rect()

    def interacted_with(self, other_tile: Tile, game: "Game") -> None:
        if not isinstance(other_tile, Player):
            return

        game.game_won()


class Enemy(TouchableTile):
    def __init__(self, path: list[Direction], chance_to_move: float = 1.0) -> None:
        self.index = 0
        self.path = path
        self.chance_to_move = chance_to_move
        super().__init__()

    def init(
        self,
        pos: tuple[int, int],
        tile_size: int,
        surfs: SurfsType,
    ) -> None:
        self.tile_size = tile_size
        self.pos = pos
        if type(self) not in surfs:
            self.surf = pygame.Surface((tile_size, tile_size), pygame.SRCALPHA)
            pygame.draw.circle(
                self.surf,
                _ENEMY_COLOR,
                (tile_size // 2, tile_size // 2),
                0.9 * tile_size // 2,
            )
            surfs[type(self)] = self.surf
        else:
            self.surf = surfs[type(self)]
        self.rect = self.surf.get_rect()

    def interacted_with(self, other_tile: Tile, game: "Game") -> None:
        if not isinstance(other_tile, Player):
            return

        game.game_over(
            "You ran into an enemy.",
            random.choice(
                [
                    "Stop touching people.",
                    "Invisibilty doesn't matter if you are running into them.",
                    "Dying isn't good for your health.",
                    "Consider not doing that.",
                    "They were just standing there. Why?",
                    "Avoid collisions!",
                    "Your enemies are not walls. Stop treating them as such.",
                ]
            ),
        )


TileVar = TypeVar("TileVar", bound=Tile)


class Map:
    def __init__(self, map: list[list[Tile | None]]) -> None:
        self.map = map
        self.height = len(map)
        self.width = len(map[0]) if map else 0
        for i, row in enumerate(map):
            if len(row) != self.width:
                raise ValueError(
                    f"Expected MxN matrix for map argument ({self.height}x{self.width}). Row {i} has a length of ({len(row)}) instead of {self.width}."
                )

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

    def get_tiles(self, cls: Type[TileVar]) -> list[TileVar]:
        """
        Find 1 or more tiles

        :return: tiles
        """
        tiles: list[TileVar] = []
        for row in self.map:
            for tile in row:
                if isinstance(tile, cls):
                    tiles.append(tile)
        return tiles
