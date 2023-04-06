import random
import pygame
from sprites.square import Square
from sprites.number1 import Number1
from sprites.number2 import Number2
from sprites.number3 import Number3
from sprites.number4 import Number4
from sprites.number5 import Number5
from sprites.number6 import Number6
from sprites.number7 import Number7
from sprites.number8 import Number8
#from sprites.hidden_mine import HiddenMine
from sprites.revealed_square import RevealedSquare
from sprites.flag import Flag


class Level:
    def __init__(self, size_x, size_y, mine_x):
        self.size_x = size_x
        self.size_y = size_y
        self.mine_x = mine_x
        self.mines = []
        self.flags=[]
        self.revealed=[]
        self.adjacent = []
        self._place_mines()
        self.all_sprites = pygame.sprite.Group()
        self.init_sprites()

    def _set_adjacents(self, _x, _y):
        if _x > 0:
            if _y < self.size_y-1:
                self.adjacent[_x-1][_y+1] += 1
            self.adjacent[_x-1][_y] += 1
            if _y > 0:
                self.adjacent[_x-1][_y-1] += 1
        if _y > 0:
            self.adjacent[_x][_y-1] += 1
            if _x < self.size_x-1:
                self.adjacent[_x+1][_y-1] += 1
        if _y < self.size_y-1:
            self.adjacent[_x][_y+1] += 1
            if _x < self.size_x-1:
                self.adjacent[_x+1][_y+1] += 1
        if _x < self.size_x-1:
            self.adjacent[_x+1][_y] += 1

    def _place_mines(self):
        for _ in range(0, self.size_x):
            self.mines.append([0]*self.size_y)
            self.adjacent.append([0]*self.size_y)
            self.flags.append([0]*self.size_y)
            self.revealed.append([0]*self.size_y)
        for _ in range(0, self.mine_x):
            while True:
                m_x = random.randint(0, self.size_x-1)
                m_y = random.randint(0, self.size_y-1)
                if self.mines[m_x][m_y] == 0:
                    self.mines[m_x][m_y] = 1
                    self._set_adjacents(m_x, m_y)
                    break

    def _get_number(self, _x, _y, norm_x, norm_y):
        _n=self.adjacent[_x][_y]
        _s=[RevealedSquare, Number1, Number2, Number3, Number4, Number5, Number6, Number7, Number8]
        return _s[_n](norm_x, norm_y)

    def init_sprites(self):
        for _x in range(0, self.size_x):
            for _y in range(0, self.size_y):
                norm_x = _x*50
                norm_y = _y*50
                if self.flags[_x][_y] == 1:
                    self.all_sprites.add(Flag(norm_x, norm_y))
                elif self.revealed[_x][_y]==1:
                    self.all_sprites.add(self._get_number(_x, _y, norm_x, norm_y))
                else:
                    self.all_sprites.add(Square(norm_x, norm_y))

    def reveal(self, _x, _y):
        if self.flags[_x][_y]==1:
            return True
        if self.mines[_x][_y] == 1:
            return False
        self.revealed[_x][_y]=1
        return True

    def draw_flag(self, _x, _y):
        if self.flags[_x][_y]==0:
            self.flags[_x][_y] = 1
        else:
            self.flags[_x][_y] = 0
