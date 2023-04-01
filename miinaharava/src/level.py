import pygame
import random
from sprites.square import Square
from sprites.number1 import Number_1
from sprites.number2 import Number_2
from sprites.number3 import Number_3
from sprites.number4 import Number_4
from sprites.number5 import Number_5
from sprites.number6 import Number_6
from sprites.number7 import Number_7
from sprites.number8 import Number_8
from sprites.hiddenMine import HiddenMine

class Level:
    def __init__(self, sizeX, sizeY, mineX):
        self.sizeX=sizeX
        self.sizeY=sizeY
        self.mineX=mineX
        self.grid=[]
        self.adjacent=[]
        self._place_mines()
        self.squares=pygame.sprite.Group()
        self.all_sprites=pygame.sprite.Group() 
        self._init_sprites()       
    
    def _place_mines(self):
        for i in range(0, self.sizeX):
            row=[]
            rowA=[]
            for j in range(0, self.sizeY):
                row.append(0)
                rowA.append(0)
            self.grid.append(row)
            self.adjacent.append(rowA)
        for i in range(0, self.mineX):
            while True:
                mX=random.randint(0, self.sizeX-1)
                mY=random.randint(0, self.sizeY-1)
                if self.grid[mX][mY]==0:
                    self.grid[mX][mY]=1
                    if mX>0:
                        if mY<self.sizeY-1:
                            self.adjacent[mX-1][mY+1]+=1
                        self.adjacent[mX-1][mY]+=1
                        if mY>0:
                            self.adjacent[mX-1][mY-1]+=1
                    if mY>0:
                        self.adjacent[mX][mY-1]+=1
                        if mX<self.sizeX-1:
                            self.adjacent[mX+1][mY-1]+=1
                    if mY<self.sizeY-1:
                        self.adjacent[mX][mY+1]+=1
                        if mX<self.sizeX-1:
                            self.adjacent[mX+1][mY+1]+=1
                    if mX<self.sizeX-1:
                        self.adjacent[mX+1][mY]+=1
                    break
    
    def _init_sprites(self):
        for x in range(0, self.sizeX):
            for y in range(0, self.sizeY):
                sqr=self.grid[x][y]
                normX=x*50
                normY=y*50
                if self.grid[x][y]==1:
                    self.squares.add(HiddenMine(normX, normY))
                else:
                    self.squares.add(Square(normX, normY))
        self.all_sprites.add(self.squares)