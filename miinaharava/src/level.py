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
from sprites.hover_square import HoverSquare
from sprites.revealed_square import RevealedSquare
from sprites.flag import Flag
from sprites.win import Win
from sprites.lose import Lose
from sprites.found_mine import FoundMine


class Level:
    """Luokka, joka sisältää tiedot pelattavasta ruudukosta ja klikatuista ruuduista

    Attributes:
        mine_x: miinojen määrä
        size: ruudukon leveys ja korkeus
        mines: miinojen sijainnit
        revealed: ruutujen tilanne
        adjacent: ruutuja ympäröivien miinojen määrä
        hovered: koordinaatit ruudulle, jonka päällä kursori on
        win: voiton/häviön tilanne
    """
    def __init__(self, size_x, size_y, mine_x):
        """Luokan konstruktori, joka luo uuden ruudukon

        Args:
            size_x: ruudukon leveys
            size_y: ruudukon korkeus
            mine_x: miinojen määrä
        """
        self.mine_x = mine_x
        self.size = (size_x, size_y)
        self.mines = []
        self.revealed = []
        self.adjacent = []
        self.hovered = None
        self.win = 0
        self._place_mines()
        self.all_sprites = pygame.sprite.Group()
        self.init_sprites()

    def _set_adjacents(self, _x, _y):
        """Määrittää ruudulle, kuinka monta miinaa viereisissä ruuduissa on

        Args:
            _x: ruudun x-koordinaatti
            _y: ruudun y-koordinaatti
        """
        if _x > 0:
            if _y < self.size[1]-1:
                self.adjacent[_x-1][_y+1] += 1
            self.adjacent[_x-1][_y] += 1
            if _y > 0:
                self.adjacent[_x-1][_y-1] += 1
        if _y > 0:
            self.adjacent[_x][_y-1] += 1
            if _x < self.size[0]-1:
                self.adjacent[_x+1][_y-1] += 1
        if _y < self.size[1]-1:
            self.adjacent[_x][_y+1] += 1
            if _x < self.size[0]-1:
                self.adjacent[_x+1][_y+1] += 1
        if _x < self.size[0]-1:
            self.adjacent[_x+1][_y] += 1

    def _place_mines(self):
        """Määrittää miinojen paikat ja muodostaa matriisit
        """
        for _ in range(0, self.size[0]):
            self.mines.append([0]*self.size[1])
            self.adjacent.append([0]*self.size[1])
            self.revealed.append([0]*self.size[1])
        for _ in range(0, self.mine_x):
            while True:
                m_x = random.randint(0, self.size[0]-1)
                m_y = random.randint(0, self.size[1]-1)
                if self.mines[m_x][m_y] == 0:
                    self.mines[m_x][m_y] = 1
                    self._set_adjacents(m_x, m_y)
                    break

    def _get_number(self, _x, _y, norm_x, norm_y):
        """Hakee sopivan spriten paljastetulle ruudulle

        Args:
            _x: ruudun x-koordinaatti
            _y: ruudun y-koordinaatti
            norm_x: näytön x-koordinaatti
            norm_y: näytön y-koordinaatti
        
        Returns:
            Piirrettävä sprite
        """
        _n = self.adjacent[_x][_y]
        _s = [RevealedSquare, Number1, Number2, Number3,
              Number4, Number5, Number6, Number7, Number8]
        return _s[_n](norm_x, norm_y)

    def init_sprites(self):
        """Lisää näytölle piirrettävät spritet ryhmään
        """
        self.all_sprites.empty()
        for _x in range(0, self.size[0]):
            for _y in range(0, self.size[1]):
                norm_x = _x*50
                norm_y = _y*50
                if self.revealed[_x][_y]==3:
                    self.all_sprites.add(FoundMine(norm_x, norm_y))
                elif (not self.hovered is None) and self.hovered[0] == _x and self.hovered[1] == _y:
                    self.all_sprites.add(HoverSquare(norm_x, norm_y))
                elif self.revealed[_x][_y] == 2:
                    self.all_sprites.add(Flag(norm_x, norm_y))
                elif self.revealed[_x][_y] == 1:
                    self.all_sprites.add(
                        self._get_number(_x, _y, norm_x, norm_y))
                else:
                    self.all_sprites.add(Square(norm_x, norm_y))
        if self.win == -1:
            self.all_sprites.add(
                Win((self.size[0]*50)/2-125, (self.size[1]*50)/2-75))
        elif self.win == -2:
            self.all_sprites.add(
                Lose((self.size[0]*50)/2-125, (self.size[1]*50)/2-75))

    def hover(self, _x, _y):
        """Määrittää korostetun ruudun koordinaatit

        Args:
            _x: ruudun x-koordinaatti
            _y: ruudun y-koordinaatti
        """
        if self.win < 0:
            self.hovered = None
            return
        if self.revealed[_x][_y] == 1 or self.revealed[_x][_y] == 2:
            self.hovered = None
            return
        self.hovered = (_x, _y)

    def check_game_end(self):
        """Tarkistaa, onko peli voitettu
        """
        if not self.win == self.size[0]*self.size[1]:
            return
        for _x in range(0, self.size[0]):
            for _y in range(0, self.size[1]):
                if self.revealed[_x][_y] == 2 and (not self.mines[_x][_y] == 1):
                    return
        self.win = -1

    def move_mine(self, _x, _y):
        """Siirtää miinan toiseen ruutuun

        Args:
            _x: ruudun x-koordinaatti
            _y: ruudun y-koordinaatti
        """
        self.mines[_x][_y] = 0
        for _i in range(0, self.size[0]):
            for _j in range(0, self.size[1]):
                if self.mines[_i][_j] == 0:
                    self.mines[_i][_j] = 1
                    return

    def recur_reveal(self, _x, _y):
        """Paljastaa jokaisen vierekkäisen ruudun

        Args:
            _x: ruudun x-koordinaatti
            _y: ruudun y-koordinaatti
        """
        self.reveal(_x-1, _y+1, False)
        self.reveal(_x, _y+1, False)
        self.reveal(_x+1, _y+1, False)
        self.reveal(_x-1, _y, False)
        self.reveal(_x+1, _y, False)
        self.reveal(_x-1, _y-1, False)
        self.reveal(_x, _y-1, False)
        self.reveal(_x+1, _y-1, False)

    def reveal(self, _x, _y, first_click):
        """Paljastaa valitun ruudun

        Args:
            _x: ruudun x-koordinaatti
            _y: ruudun y-koordinaatti
            first_click: onko tämä ensimmäinen klikattu ruutu (True/False)
        """
        if (_x < 0 or _x > self.size[0]-1) or (_y < 0 or _y > self.size[1]-1):
            return
        if self.win < 0:
            return
        if self.revealed[_x][_y] == 1 or self.revealed[_x][_y] == 2:
            return
        if self.mines[_x][_y] == 1:
            if first_click:
                self.move_mine(_x, _y)
            else:
                self.revealed[_x][_y]=3
                self.win = -2
                return
        self.revealed[_x][_y] = 1
        self.hovered = None
        if self.adjacent[_x][_y] == 0:
            self.recur_reveal(_x, _y)
        self.win += 1
        self.check_game_end()

    def draw_flag(self, _x, _y):
        """Sijoittaa lipun ruutuun

        Args:
            _x: ruudun x-koordinaatti
            _y: ruudun y-koordinaatti
        """
        if self.win < 0:
            return
        if self.revealed[_x][_y] == 1:
            return
        if self.revealed[_x][_y] == 0:
            self.hovered = None
            self.revealed[_x][_y] = 2
            self.win += 1
        else:
            self.revealed[_x][_y] = 0
            self.win -= 1
        self.check_game_end()
