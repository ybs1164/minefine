import pygame

class Cell:
    def __init__(self, isMine):
        self.isMine = isMine
        self.isEnable = False
        self.isFlag = False
        self.closecells = []

    def isGameOver(self):
        if self.isMine and self.isEnable:
            return True
        return False

    def setCloseCells(self, closecells):
        self.closecells = closecells

    def getMineCount(self):
        if self.isFlag:
            return -3
        if not self.isEnable:
            return -1
        if self.isMine:
            return -2
        
        cnt = 0
        for i in self.closecells:
            if i.isMine:
                cnt += 1
        return cnt
    
