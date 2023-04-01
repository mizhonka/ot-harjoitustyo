import pygame
import random
from sprites.square import Square

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
                self.squares.add(Square(normX, normY))
        self.all_sprites.add(self.squares)