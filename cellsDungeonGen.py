import pygame
import random
import time

INITIALPROB=0.9
ALIVELIMIT=5
DIELIMIT=4

CELLWIDTH=1

XCELLSNUM=10
YCELLSNUM=10

SEPWIDTH=0

windowWidth=(XCELLSNUM+1)*SEPWIDTH+XCELLSNUM*CELLWIDTH
windowHeight=(YCELLSNUM+1)*SEPWIDTH+YCELLSNUM*CELLWIDTH


class Cell:
    def __init__(self,x,y,isAlive):
        self.x=x
        self.y=y
        self.isAlive=isAlive

    def alive(self):
        self.isAlive=True

    def die(self):
        self.isAlive=False


class Cells:
    def __init__(self,w,h,screen):
        self.width=w
        self.height=h
        self.screen=screen
        self.nextCellsArray=[]
        self.cellsArray=[]
        for i in range(self.height):
            self.cellsArray.append([])
            self.nextCellsArray.append([])
            for j in range(self.width):
                self.cellsArray[i].append(Cell(j,i,(True if INITIALPROB>random.random() else False)))
                self.nextCellsArray[i].append(Cell(j,i,False))
        
    def drawCells(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.cellsArray[y][x].isAlive:
                    pygame.draw.rect(self.screen,(255,255,255),((x+1)*SEPWIDTH+x*CELLWIDTH,(y+1)*SEPWIDTH+y*CELLWIDTH,CELLWIDTH,CELLWIDTH))

    def updateGen(self):
        for y in range(self.height):
            for x in range(self.width):
                self.nextState(x,y)

        for y in range(self.height):
            for x in range(self.width):
                self.cellsArray[y][x]=self.nextCellsArray[y][x]

    def nextState(self,x,y):
        count=self.countAroundCell(x,y)
        if self.cellsArray[y][x].isAlive:
            if count<DIELIMIT:
                self.nextCellsArray[y][x].die()
            else:
                self.nextCellsArray[y][x].alive()
        else:
            if count>ALIVELIMIT:
                self.nextCellsArray[y][x].alive()
            else:
                self.nextCellsArray[y][x].die()

    def countAroundCell(self,x,y):
        count=0
        for i in range(-1,2):
            for j in range(-1,2):
                if not(i == 1 and j == 1) and y+i>=0 and y+i<self.height and x+j>=0 and x+j<self.width:
                    if self.cellsArray[y+i][x+j].isAlive:
                        count+=1
        return count




def main():
    pygame.init()
    screen = pygame.display.set_mode((windowWidth, windowHeight))
    cells=Cells(XCELLSNUM,YCELLSNUM,screen)

    while True:
        screen.fill((0,0,0))
        cells.drawCells()
        cells.updateGen()
        pygame.display.update()
        time.sleep(1)

if __name__=='__main__':
    main()

