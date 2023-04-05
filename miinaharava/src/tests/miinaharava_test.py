import unittest
import pygame
from level import Level


class TestLevel(unittest.TestCase):
    def test_grid_parameters(self):
        x = 9
        y = 9
        m = 10
        level = Level(x, y, m)
        self.assertEqual(x, level.sizeX)
        self.assertEqual(y, level.sizeY)
        self.assertEqual(m, level.mineX)
