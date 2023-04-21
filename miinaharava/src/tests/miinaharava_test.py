import unittest
import pygame
from level import Level
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
from sprites.win import Win
from sprites.lose import Lose


class TestLevel(unittest.TestCase):
    def test_grid_parameters(self):
        x = 9
        y = 9
        m = 10
        level = Level(x, y, m)
        self.assertEqual(x, level.size[0])
        self.assertEqual(y, level.size[1])
        self.assertEqual(m, level.mine_x)
    
    def test_sprite_rect(self):
        ss = [Square, HoverSquare, Flag, Win, Lose, RevealedSquare, Number1, Number2, Number3,
              Number4, Number5, Number6, Number7, Number8]
        for s in ss:
            s=s()
            assert s.rect is not None
            self.assertEqual(0, s.rect.x)
            self.assertEqual(0, s.rect.y)
