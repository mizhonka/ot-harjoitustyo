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
from sprites.hidden_mine import HiddenMine
from sprites.flag import Flag


class Level:
    def __init__(self, size_x, size_y, mine_x):
        self.size_x = size_x
        self.size_y = size_y
        self.mine_x = mine_x
        self.grid = []
        self.adjacent = []
        self._place_mines()
        self.squares = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self._init_sprites()

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
            row = []
            row_a = []
            for _ in range(0, self.size_y):
                row.append(0)
                row_a.append(0)
            self.grid.append(row)
            self.adjacent.append(row_a)
        for _ in range(0, self.mine_x):
            while True:
                m_x = random.randint(0, self.size_x-1)
                m_y = random.randint(0, self.size_y-1)
                if self.grid[m_x][m_y] == 0:
                    self.grid[m_x][m_y] = 1
                    self._set_adjacents(m_x, m_y)
                    break

    def _init_sprites(self):
        for _x in range(0, self.size_x):
            for _y in range(0, self.size_y):
                norm_x = _x*50
                norm_y = _y*50
                if self.grid[_x][_y] == 1:
                    self.squares.add(HiddenMine(norm_x, norm_y))
                elif self.grid[_x][_y] == 2:
                    print("flag found")
                    self.squares.add(Flag(norm_x, norm_y))
                else:
                    self.squares.add(Square(norm_x, norm_y))
        self.all_sprites.add(self.squares)

    def reveal(self, _x, _y):
        if self.grid[_x][_y] == 1:
            return False
        return True

    def draw_flag(self, _x, _y):
        self.grid[_x][_y] = 2
