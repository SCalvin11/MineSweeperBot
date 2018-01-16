import pyautogui as pag

class Tile():
    def __init__(self, x, y, topleft):
        self.x = x
        self.y = y
        self.topLeft = topleft
        self.screenPosition = self.findPosition()
        self.mine = False
        self.flagged = False
        self.hasBeenLeftClicked = False
        self.number = None
        self.surrounding = []

    def __str__(self):
        return "N:{} xy:{},{}".format(self.number, self.x, self.y)

    def __repr__(self):
        return self.__str__()

    def findPosition(self):
        # pag.moveTo(self.topLeft[0] + (20 * self.x) + 5, self.topLeft[1] + (20 * self.y) + 5,.5)
        return (self.topLeft[0] + (20 * self.x) + 5, self.topLeft[1] + (20 * self.y) + 5)

    def updateNumber(self, num):
        self.number = num

        if num < 9:
            self.couldBeAMine = False

    def updateSurrounding(self, board):
        surrounding = []

        if (self.x > 0):
            surrounding.append(board[self.y][self.x - 1])
        if (self.y > 0):
            surrounding.append(board[self.y - 1][self.x ])
        if (self.y > 0) and (self.x > 0):
            surrounding.append(board[self.y - 1][self.x - 1])
        if (self.x < 8):
            surrounding.append(board[self.y][self.x + 1])
        if (self.y < 8):
            surrounding.append(board[self.y + 1][self.x ])
        if (self.x < 8) and (self.y < 8):
            surrounding.append(board[self.y + 1][self.x + 1])
        if (self.y > 0) and (self.x < 8):
            surrounding.append(board[self.y - 1][self.x + 1])
        if (self.x > 0) and (self.y < 8):
            surrounding.append(board[self.y + 1][self.x - 1])

        self.surrounding = surrounding


# 012345678
# 012345678
# 012345678
# 012345678
# 012345678
# 012345678
# 012345678
# 012345678
# 012345678
