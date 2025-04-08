import sys
import pygame
from pygame import locals


class Game:

    clock = pygame.time.Clock()
    DEFAULT_WIDTH = 1280
    DEFAULT_HEIGHT = 720
    MAX_FPS = 120
    MSPT = 500
    """Millisecond per tick"""
    TITLE = "Maze Game"

    def __init__(self) -> None:
        pygame.init()
        self.displaysurface = pygame.display.set_mode(
            (self.DEFAULT_WIDTH, self.DEFAULT_HEIGHT), locals.RESIZABLE
        )
        pygame.display.set_caption(self.TITLE)
        self.delta_ms = 0.0
        self.tick_delta_ms = 0.0
        """Time delta in milisecond"""

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
        pass

    def update(self) -> bool:
        """
        The game logic that occurs within a frame.

        :return: Whether the game should end
        """
        for event in pygame.event.get():
            if event.type == locals.QUIT:
                self.teardown()
                return True

        if self.tick_delta_ms > self.MSPT:
            self.tick_delta_ms -= self.MSPT
            self.tick()

        self.time_delta = self.clock.tick(self.MAX_FPS)
        self.tick_delta_ms += self.time_delta
        return False
