class Cell:
    def __init__(self, isMine):
        self.isMine = isMine
        self.isEnable = False
        self.isFlag = False
        #self.closecells = []
        self.mineCount = 0

    #
    def getMineCount(self):
        if self.isFlag and not self.isEnable:
            return -3
        if not self.isEnable:
            return -1
        if self.isMine:
            return -2
        
        return self.mineCount

'''
    def setCloseCells(self, closecells):
        self.closecells = closecells
        cnt = 0
        for i in self.closecells:
            if i.isMine:
                cnt += 1
        self.mineCount = cnt
'''
    
