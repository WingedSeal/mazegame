import sys
import pygame
from pygame import locals
from pygame.math import Vector2

from .map import Map, Tile


class Game:

    clock = pygame.time.Clock()
    DEFAULT_WIDTH = 1280
    DEFAULT_HEIGHT = 720
    MAX_FPS = 120
    MSPT = 2000
    """Millisecond per tick"""
    TITLE = "Maze Game"
    BG_COLOR = pygame.Color(10, 10, 10)

    def __init__(self, map: Map) -> None:
        pygame.init()
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

    def run(self) -> None:
        """
        Starts game loop
        """
        while True:
            if self.update():
                break
        sys.exit()

    def tick(self) -> None:
        self.moving_tiles = []
        self.try_move_tile(2, 2, -1, -1)

    def update(self) -> bool:
        """
        The game logic that occurs within a frame.

        :return: Whether the game should end
        """
        for event in pygame.event.get():
            if event.type == locals.QUIT:
                self.teardown()
                return True

        self.display_surface.fill(self.BG_COLOR)

        if self.tick_delta_ms > self.MSPT:
            self.tick_delta_ms -= self.MSPT
            self.tick()

        t = self.tick_delta_ms / self.MSPT
        for tile in self.moving_tiles:
            tile.animate(t)
        for y, row in enumerate(self.map.map):
            for x, tile in enumerate(row):
                if tile is None:
                    continue

                assert hasattr(tile, "surf")
                assert hasattr(tile, "rect")
                self.display_surface.blit(tile.surf, tile.rect)

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
        if self.map.map[y + dy][x + dx] is not None:
            return False
        tile = self.map.map[y][x]
        if tile is None:
            return False
        tile.old_pos = tile.pos
        tile.pos = (x + dx, y + dy)
        self.map.map[y + dy][x + dx] = tile
        self.map.map[y][x] = None
        self.moving_tiles.append(tile)
        return True

    def render_map(self) -> None:
        pass
