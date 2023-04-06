import os
import pygame
dirname = os.path.dirname(__file__)


class Win(pygame.sprite.Sprite):
    def __init__(self, _x=0, _y=0):
        super().__init__()
        self.image = pygame.image.load(
            os.path.join(dirname, "..", "assets", "win.png"))
        self.rect = self.image.get_rect()
        self.rect.x =_x
        self.rect.y = _y
