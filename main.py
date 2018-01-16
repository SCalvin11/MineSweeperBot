import pyautogui as pag
import time

from Board import Board
from BotLogic import BotLogic\

def test():
    pag.click(x=board.topLeft[0] - 5, y=board.topLeft[1] - 5)
    logic.firstClick()
    while True:
        mines = logic.checkEasy()
        logic.rightClickList(mines)

        safe = logic.checkEasyMines()
        logic.leftClickList(safe)

        oneTwoOne = logic.checkOneTwoOne()
        logic.rightClickList(oneTwoOne)

        board.scanTiles()

if __name__ == "__main__":
    board = Board()
    board.getAnchor()
    # pag.click(board.topLeft[0], board.topLeft[1])
    # pag.click(board.topLeft[0] + 10 + 40, board.topLeft[1] + 10 + 80)
    board.scanTiles()
    board.updateTilesSurrounding()
    # board.printBoard()
    logic = BotLogic(board)
    test()
