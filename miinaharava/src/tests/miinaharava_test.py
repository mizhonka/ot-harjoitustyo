import unittest
import pygame
from level import Level
from ui.ui import Game
from sprites.square import Square
from sprites.number1 import Number1
from sprites.number2 import Number2
from sprites.number3 import Number3
from sprites.number4 import Number4
from sprites.number5 import Number5
from sprites.number6 import Number6
from sprites.number7 import Number7
from sprites.number8 import Number8
from sprites.hover_square import HoverSquare
from sprites.revealed_square import RevealedSquare
from sprites.flag import Flag
from sprites.end_screen import EndScreen
from sprites.easy import Easy
from sprites.easy_light import EasyLight
from sprites.medium import Medium
from sprites.medium_light import MediumLight
from sprites.hard import Hard
from sprites.hard_light import HardLight
from sprites.found_mine import FoundMine


class TestLevel(unittest.TestCase):
    def setUp(self):
        self.x = 9
        self.y = 9
        self.m = 10
        self.level = Level(self.x, self.y, self.m)
        self.game = Game()

    def test_grid_parameters(self):
        self.assertEqual(self.x, self.level.size[0])
        self.assertEqual(self.y, self.level.size[1])
        self.assertEqual(self.m, self.level.mine_x)

    def test_sprite_rect(self):
        ss = [Square, HoverSquare, Flag, EndScreen, RevealedSquare, Number1, Number2, Number3,
              Number4, Number5, Number6, Number7, Number8, Easy, EasyLight, Medium, MediumLight, Hard, HardLight, FoundMine]
        for s in ss:
            s = s()
            assert s.rect is not None
            self.assertEqual(0, s.rect.x)
            self.assertEqual(0, s.rect.y)

    def test_no_hover_when_end(self):
        if self.level.win < 0:
            assert self.level.hovered is None

    def test_level_parameters(self):
        self.game.set_level(self.x, self.y, self.m)
        self.assertEqual(self.x, self.game.level_x)
        self.assertEqual(self.y, self.game.level_y)
        self.assertEqual(self.m, self.game.mine_x)
    
    def test_wrong_flags_no_win(self):
        for i in range(self.x):
            for j in range(self.y):
                self.level.draw_flag(i, j)
        self.assertNotEqual(self.level.win, -1)
    
    def test_no_flags_after_end(self):
        self.level.win=-1
        self.assertEqual(self.level.draw_flag(0,0), 0)
        self.level.win=-2
        self.assertEqual(self.level.draw_flag(0,0), 0)
    
    def test_dont_reveal_revealed(self):
        self.level.reveal(0, 0, True)
        self.assertEqual(self.level.reveal(0, 0, False), False)
    
    def test_reveal_adjacents(self):
        for i in range(1, self.x-1):
            for j in range(1, self.y-1):
                if self.level.adjacent[i][j]==0:
                    self.level.reveal(i, j, True)
                    self.assertEqual(self.level.revealed[i-1][j+1], 1)
                    self.assertEqual(self.level.revealed[i][j+1], 1)
                    self.assertEqual(self.level.revealed[i+1][j+1], 1)
                    self.assertEqual(self.level.revealed[i-1][j], 1)
                    self.assertEqual(self.level.revealed[i+1][j], 1)
                    self.assertEqual(self.level.revealed[i-1][j-1], 1)
                    self.assertEqual(self.level.revealed[i][j-1], 1)
                    self.assertEqual(self.level.revealed[i+1][j-1], 1)
                    break
