import unittest
import pygame
from level import Level


class TestLevel(unittest.TestCase):
    def test_grid_parameters(self):
        x = 9
        y = 9
        m = 10
        level = Level(x, y, m)
        self.assertEqual(x, level.size_x)
        self.assertEqual(y, level.size_y)
        self.assertEqual(m, level.mine_x)
