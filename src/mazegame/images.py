import pygame

from .color import Color


class Images:
    def __init__(self) -> None:
        self.surfaces: dict[str, pygame.Surface] = {}

    def get_surface(self, name: str) -> pygame.Surface:
        if name not in self.surfaces:
            self.surfaces[name] = pygame.image.load(
                f"assets/sprite/{name}.jpg"
            ).convert()
        return self.surfaces[name]
