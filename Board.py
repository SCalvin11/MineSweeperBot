import pyautogui as pag
from tile import Tile

OFFSET_TO_ANCHOR = 6
TILE_SIZE = 20
WIDTH = 180
HEIGHT = 180

class Board():
    def __init__(self):
        self.topLeft = self.getAnchor()
        # self.board = [
        #     [9,9,9,9,9,9,9,9,9],
        #     [9,9,9,9,9,9,9,9,9],
        #     [9,9,9,9,9,9,9,9,9],
        #     [9,9,9,9,9,9,9,9,9],
        #     [9,9,9,9,9,9,9,9,9],
        #     [9,9,9,9,9,9,9,9,9],
        #     [9,9,9,9,9,9,9,9,9],
        #     [9,9,9,9,9,9,9,9,9],
        #     [9,9,9,9,9,9,9,9,9]]
        self.tileList = []
        self.board = self.generateBoard(self.tileList)
        self.tilePics = ['img/blank_tile.png', 'img/one_block.png',
                    'img/two_block.png', 'img/three_block.png',
                    'img/four_block.png', 'img/five_block.png',
                    'img/six_block.png', 'img/seven_block.png',
                    'img/eight_block.png',
                    'img/covered_block.png']

    def generateBoard(self, tileList):
        board = [[],[],[],[],[],[],[],[],[]]
        for i in range(9):
            for j in range(9):
                tile = Tile(j, i, self.topLeft)
                board[i].append(tile)
                tileList.append(tile)

        return board


    def printBoard(self):
        i = 0
        while i < len(self.board):
            print(self.board[i])
            i += 1

    def updateCell(self, row, col, value):
        self.board[col][row].updateNumber(value)

    def getAnchor(self):
        anchor = pag.locateOnScreen('img/anchor.png')
        return (anchor[0] + OFFSET_TO_ANCHOR, anchor[1] + OFFSET_TO_ANCHOR)

    def updateTilesSurrounding(self):
        for i in range(9):
            for j in range(9):
                self.board[i][j].updateSurrounding(self.board)

    def scanTiles(self):
        counter = 0
        for i in self.tilePics:
            ones = list(pag.locateAllOnScreen(i, region=(self.topLeft[0], self.topLeft[1], WIDTH, HEIGHT)))

            for one in ones:
                x = (one[0] - self.topLeft[0]) // TILE_SIZE
                y = (one[1] - self.topLeft[1]) // TILE_SIZE
                if (x >= 0 and x <=8) and (y >= 0 and y <= 8):
                    self.updateCell(x, y, counter)
            counter += 1
