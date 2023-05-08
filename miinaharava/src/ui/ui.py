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
    """Luokka, joka luo uuden pelin ja käsittelee pelaajan syötteen

    Attributes:
        level_x: ruudukon leveys
        level_y: ruudukon korkeus
        mine_x: miinojen määrä
    """

    def __init__(self):
        """Luokan konstruktori
        """
        pygame.init()
        self.level_x = 0
        self.level_y = 0
        self.mine_x = 0
        self.font=pygame.font.SysFont("Arial", 90)
        self.mineText=self.font.render("0", True, (0,0,0))
        self.timerText=self.font.render("0", True, (0,0,0))
    
    def change_mine_text(self, x):
        self.mineText=self.font.render(str(x), True, (0,0,0))

    def set_level(self, x, y, m):
        """Asettaa ruudukon tiedot

        Args:
            x: ruudukon leveys
            y: ruudukon korkeus
            x: miinojen määrä
        """
        self.level_x = x
        self.level_y = y
        self.mine_x = m

    def mouse_pos(self):
        """Hakee kursorin sijainnin

        Returns:
            Kursorin sijainnin koordinaatit tuplena ruutuihin suhteutettuna
        """
        if not pygame.mouse.get_focused():
            return
        pos = pygame.mouse.get_pos()
        return (int(math.modf(pos[0]/50)[1]), int(math.modf(pos[1]/50)[1]))

    def main(self):
        """Luo Level-olion ja käsittelee pelaajan syötteen
        """
        display = pygame.display.set_mode((self.level_x*50, self.level_y*50+100))
        pygame.display.set_caption("Miinaharava")
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        level = Level(self.level_x, self.level_y, self.mine_x)
        running = True
        first_click = True
        timer=0
        while running:
            cords = self.mouse_pos()
            if cords:
                level.hover(cords[0], cords[1])
            else:
                level.hover(-1, -1)
            for event in pygame.event.get():
                if event.type==pygame.USEREVENT:
                    self.timerText=self.font.render(str(timer), True, (0,0,0))
                    timer+=1
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
            display.fill((200,200,200))
            level.all_sprites.draw(display)
            display.blit(self.mineText, (50,self.level_y*50))
            display.blit(self.timerText, (self.level_x*50-100, self.level_y*50))
            pygame.display.update()
        pygame.quit()

    def add_buttons(self, v):
        """Lisää oikeat valikkonapit ryhmään

        Args:
            v: vaikeusaste
        """
        self.buttons.empty()
        if v == 0:
            self.buttons.add(EasyLight(0, 0))
        else:
            self.buttons.add(Easy(0, 0))
        if v == 1 or v == 2:
            self.buttons.add(MediumLight(0, 75))
        else:
            self.buttons.add(Medium(0, 75))
        if v == 3 or v == 4:
            self.buttons.add(HardLight(0, 150))
        else:
            self.buttons.add(Hard(0, 150))

    def difficulty(self):
        """Luo vaikeusaste-valikon ja käsittelee pelaajan syötteen
        """
        display = pygame.display.set_mode((250, 3*75))
        pygame.display.set_caption("Miinaharava")
        pygame.init()
        self.buttons = pygame.sprite.Group()
        v = -1
        running = True
        while running:
            cords = self.mouse_pos()
            if cords:
                v = cords[1]
            else:
                v=-1
            self.add_buttons(v)
            self.buttons.draw(display)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    running = False
        if v == 0:
            self.set_level(9, 9, 10)
        elif v == 1 or v == 2:
            self.set_level(16, 16, 40)
        elif v == 3 or v == 4:
            self.set_level(30, 16, 99)
        self.change_mine_text(self.mine_x)
        self.main()
