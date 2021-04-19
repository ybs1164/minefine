class Cell:
    def __init__(self, isMine):
        self.isMine = isMine
        self.isEnable = False
        self.isFlag = False
        self.mineCount = 0

    def getMineCount(self):
        if self.isFlag and not self.isEnable:
            return -3
        if not self.isEnable:
            return -1
        if self.isMine:
            return -2
        
        return self.mineCount