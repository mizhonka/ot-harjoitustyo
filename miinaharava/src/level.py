import pygame
import random
from sprites.square import Square

class Level:
    def __init__(self, sizeX, sizeY, mineX):
        self.sizeX=sizeX
        self.sizeY=sizeY
        self.grid=[]
        self.adjacent=[]
        for i in range(0, sizeX):
            row=[]
            rowA=[]
            for j in range(0, sizeY):
                row.append(0)
                rowA.append(0)
            self.grid.append(row)
            self.adjacent.append(rowA)
        for i in range(0, mineX):
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