from dataclasses import dataclass
from enum import Enum, auto
from pathlib import Path
import random
import sys
import threading
from typing import TYPE_CHECKING
import pygame
from pygame import locals
import numpy as np
import scipy
from scipy.ndimage import gaussian_filter

from .direction import Direction
from .map import Enemy, Map, Player, Tile, TouchableTile
from .control import Control


def apply_blur(surface: pygame.Surface, radius: float) -> pygame.Surface:
    """
    Apply guassian blur to a surface

    :param surface: Original surface
    :param radius: How blurly it should be, defaults to 1
    :return: Blured surface
    """
    surf_array = pygame.surfarray.array3d(surface)
    blurred = gaussian_filter(surf_array, sigma=(radius, radius, 0))
    return pygame.surfarray.make_surface(blurred.astype(np.uint8))


class GameState(Enum):
    GAMEPLAY = auto()
    GAME_OVER = auto()


@dataclass
class GameOverData:
    last_frame: pygame.Surface | None
    dark_overlay: pygame.Surface
    heading_surface: pygame.Surface
    subheading_surface: pygame.Surface
    tips_surface: pygame.Surface


@dataclass
class GameFont:
    PATH = Path(__file__).parent / "font.ttf"
    heading: pygame.font.Font
    subheading: pygame.font.Font
    tips: pygame.font.Font


class Game:
    clock = pygame.time.Clock()
    DEFAULT_WIDTH = 1280
    DEFAULT_HEIGHT = 720
    MAX_FPS = 120
    MSPT = 500
    """Millisecond per tick"""
    TITLE = "Maze Game"
    BG_COLOR = pygame.Color(10, 10, 10)
    game_event = threading.Event()
    next_moves: list[tuple[int, int, int, int]] = []
    """Moves set by Control (pos_x, pos_y, dx, dy)"""
    is_control_alive = True

    def __init__(self, map: Map) -> None:
        self.state = GameState.GAMEPLAY
        self.game_over_data: GameOverData | None = None
        self.control = Control(map, self)
        self.enemies = map.get_tiles(Enemy)
        self.players = map.get_tiles(Player)
        for i, player in enumerate(self.players):
            player.index = i
        pygame.init()
        pygame.font.init()
        self.fonts = GameFont(
            heading=pygame.font.SysFont("Times New Roman", 40),
            subheading=pygame.font.SysFont("Times New Roman", 20),
            tips=pygame.font.SysFont("Times New Roman", 10),
            # heading=pygame.font.Font(GameFont.PATH, 20),
            # subheading=pygame.font.Font(GameFont.PATH, 20),
            # tips=pygame.font.Font(GameFont.PATH, 20),
        )
        self.game_event.set()
        self.map = map
        self.tile_size, self.screen_width, self.screen_height = self._get_tile_size()
        self.display_surface = pygame.display.set_mode(
            (self.screen_width, self.screen_height)
        )
        pygame.display.set_caption(self.TITLE)
        self.delta_ms = 0.0
        self.tick_delta_ms = 0.0
        self.moving_tiles: list[Tile] = []
        """Time delta in milisecond"""
        for y, row in enumerate(self.map.map):
            for x, tile in enumerate(row):
                if tile is not None:
                    tile.init((x, y), self.tile_size)
                    tile.rect.topleft = tile.get_top_left((x, y))

    def _get_tile_size(self) -> tuple[int, int, int]:
        """
        Calculate tile size in pixel from map

        :return: Tuple of tile_size, screen_width, screen_height
        """
        max_width = self.DEFAULT_WIDTH // self.map.width
        max_height = self.DEFAULT_HEIGHT // self.map.height
        tile_size = min(max_width, max_height)
        screen_width = self.map.width * tile_size
        screen_height = self.map.height * tile_size
        return tile_size, screen_width, screen_height

    def teardown(self) -> None:
        pygame.quit()
        sys.exit()

    def _get_tile(self, x: int, y: int) -> Tile | None:
        if x < 0 or x >= self.map.width:
            return None
        if y < 0 or y >= self.map.height:
            return None
        return self.map.map[y][x]

    def get_tile(self, direction: Direction, player_index: int = 0) -> Tile | None:
        player = self.players[player_index]
        if direction == Direction.HALT:
            return player.tile_under
        return self._get_tile(
            player.pos[0] + direction.value[0], player.pos[1] + direction.value[1]
        )

    def run(self) -> None:
        """
        Starts game loop
        """
        while True:
            if self.update():
                break
        sys.exit()

    def tick(self) -> None:
        for tile in self.moving_tiles:
            tile.animate(1)
        self.moving_tiles = []

        if self.is_control_alive:
            self.game_event.clear()
            self.control.control_event.set()
            self.game_event.wait()
            for pos_x, pos_y, dx, dy in self.next_moves:
                if self.try_move_tile(pos_x, pos_y, dx, dy):
                    self.control.player_positions.append((pos_x + dx, pos_y + dy))
                else:
                    self.control.player_positions.append((pos_x, pos_y))
            self.next_moves = []

        for enemy in self.enemies:
            if random.random() >= enemy.chance_to_move:
                continue
            self.try_move_tile(
                enemy.pos[0],
                enemy.pos[1],
                enemy.path[enemy.index].value[0],
                enemy.path[enemy.index].value[1],
            )
            enemy.index = (enemy.index + 1) % len(enemy.path)

    def _update_gameplay(self) -> None:
        self.display_surface.fill(self.BG_COLOR)

        if self.tick_delta_ms > self.MSPT:
            self.tick_delta_ms -= self.MSPT
            self.tick()

        t = self.tick_delta_ms / self.MSPT
        for tile in self.moving_tiles:
            tile.animate(t)
        for row in self.map.map:
            for tile in row:
                if tile is None:
                    continue
                if any(tile is _tile for _tile in self.moving_tiles):
                    continue
                assert hasattr(tile, "surf")
                assert hasattr(tile, "rect")
                if tile.tile_under is not None:
                    self.display_surface.blit(
                        tile.tile_under.surf, tile.tile_under.rect
                    )
                self.display_surface.blit(tile.surf, tile.rect)

        for tile in self.moving_tiles:
            if tile.tile_under is not None:
                self.display_surface.blit(tile.tile_under.surf, tile.tile_under.rect)
            self.display_surface.blit(tile.surf, tile.rect)

        if self.state == GameState.GAME_OVER:
            assert self.game_over_data is not None
            self.game_over_data.last_frame = self.display_surface.copy()
            self.tick_delta_ms = 0

    def _update_gameover(self) -> None:
        assert self.game_over_data is not None
        assert self.game_over_data.last_frame is not None
        TRANSITION_MS = 500
        t = min(self.tick_delta_ms / TRANSITION_MS, 1)
        t_darken = 1 - (1 - t) ** 4
        self.display_surface.blit(
            apply_blur(self.game_over_data.last_frame, t * 4), (0, 0)
        )
        self.game_over_data.dark_overlay.fill((0, 0, 0, int(200 * t_darken)))
        self.display_surface.blit(self.game_over_data.dark_overlay, (0, 0))
        center = self.display_surface.get_rect().center
        self.display_surface.blit(
            self.game_over_data.heading_surface,
            self.game_over_data.heading_surface.get_rect(
                center=(center[0], center[1] - 20)
            ),
        )
        self.display_surface.blit(
            self.game_over_data.subheading_surface,
            self.game_over_data.subheading_surface.get_rect(
                center=(center[0], center[1] + 20)
            ),
        )
        self.display_surface.blit(
            self.game_over_data.tips_surface,
            self.game_over_data.tips_surface.get_rect(
                center=(center[0], center[1] + 40)
            ),
        )

    def game_over(self, reason: str, tips: str) -> None:
        self.state = GameState.GAME_OVER
        self.game_over_data = GameOverData(
            None,
            pygame.Surface(self.display_surface.get_size(), pygame.SRCALPHA),
            self.fonts.heading.render("You died!", True, (200, 100, 100)),
            self.fonts.subheading.render(reason, True, (200, 200, 200)),
            self.fonts.tips.render("Tips: " + tips, True, (200, 200, 200)),
        )
        self.tick_delta_ms = 0

    def update(self) -> bool:
        """
        The game logic that occurs within a frame.

        :return: Whether the game should end
        """

        for event in pygame.event.get():
            if event.type == locals.QUIT:
                self.teardown()
                return True

        match self.state:
            case GameState.GAMEPLAY:
                self._update_gameplay()
            case GameState.GAME_OVER:
                self._update_gameover()
        pygame.display.update()
        self.time_delta = self.clock.tick(self.MAX_FPS)
        self.tick_delta_ms += self.time_delta
        return False

    def try_move_tile(self, x: int, y: int, dx: int, dy: int) -> bool:
        """
        Try to move a tile, can fail

        :param x: Original Tile's x
        :param y: Original Tile's y
        :param dx: Target Tile's x
        :param dy: Target TIle's y
        :return: Whether it was successful
        """
        if y + dy >= self.map.height:
            return False
        if x + dx >= self.map.width:
            return False
        target = self.map.map[y + dy][x + dx]
        if target is not None and not isinstance(target, TouchableTile):
            return False
        tile = self.map.map[y][x]
        if tile is None:
            return False
        tile.old_pos = tile.pos
        tile.pos = (x + dx, y + dy)
        self.map.map[y + dy][x + dx] = tile
        self.map.map[y][x] = tile.tile_under
        tile.tile_under = None
        self.moving_tiles.append(tile)

        if isinstance(target, TouchableTile):
            target.interact(tile, self)
            if target.can_be_under:
                tile.tile_under = target
        return True

    def render_map(self) -> None:
        pass
