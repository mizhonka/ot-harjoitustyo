import math
import pygame
from level import Level
from sprites.easy import Easy
from sprites.easy_light import EasyLight
from sprites.medium import Medium
from sprites.medium_light import MediumLight
from sprites.hard import Hard
from sprites.hard_light import HardLight

class Game:

    def __init__(self):
        self.level_x=0
        self.level_y=0
        self.mine_x=0

    def set_level(self,x, y, m):
        self.level_x=x
        self.level_y=y
        self.mine_x=m

    def mouse_pos(self):
        pos = pygame.mouse.get_pos()
        return (int(math.modf(pos[0]/50)[1]), int(math.modf(pos[1]/50)[1]))

    def main(self):
        display = pygame.display.set_mode((self.level_x*50, self.level_y*50))
        pygame.display.set_caption("Miinaharava")
        level = Level(self.level_x, self.level_y, self.mine_x)
        pygame.init()
        running = True
        first_click = True
        while running:
            for event in pygame.event.get():
                cords = self.mouse_pos()
                level.hover(cords[0], cords[1])
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    level.reveal(cords[0], cords[1], first_click)
                    if first_click:
                        first_click = False
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 3:
                    level.draw_flag(cords[0], cords[1])
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    level = Level(self.level_x, self.level_y, self.mine_x)
            level.init_sprites()
            level.all_sprites.draw(display)
            pygame.display.update()
        pygame.quit()
    
    def add_buttons(self, v):
        self.buttons.empty()
        if v==0:
            self.buttons.add(EasyLight(0,0))
        else:
            self.buttons.add(Easy(0,0))
        if v==1 or v==2:
            self.buttons.add(MediumLight(0,75))
        else:
            self.buttons.add(Medium(0,75))
        if v==3 or v==4:
            self.buttons.add(HardLight(0,150))
        else:
            self.buttons.add(Hard(0,150))

    def difficulty(self):
        display = pygame.display.set_mode((250, 3*75))
        pygame.display.set_caption("Miinaharava")
        pygame.init()
        self.buttons=pygame.sprite.Group()
        v=0
        running=True
        while running:
            cords=self.mouse_pos()
            v=cords[1]
            self.add_buttons(v)
            self.buttons.draw(display)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    running=False
        if v==0:
            self.set_level(9, 9, 10)
        elif v==1 or v==2:
            self.set_level(16,16,40)
        elif v==3 or v==4:
            self.set_level(30, 16, 99)
        self.main()