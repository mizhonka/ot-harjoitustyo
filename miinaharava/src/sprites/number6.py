import os
import pygame
dirname = os.path.dirname(__file__)


class Number6(pygame.sprite.Sprite):
    def __init__(self, _x=0, _y=0):
        super().__init__()
        self.image = pygame.image.load(os.path.join(
            dirname, "..", "assets", "number6.png"))
        self.rect = self.image.get_rect()
        self.rect._x = _x
        self.rect._y = _y
