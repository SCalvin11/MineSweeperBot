import Board
import time
import pyautogui as pag
import random

CLICK_DELAY = 0.01

class BotLogic():
    def __init__(self, board):
        self.board = board
        self.tiles = board.tileList

    def checkEasy(self):
        toDelete = []
        for i in self.tiles:
            numBlanks = 0
            for j in i.surrounding:
                if j.number == 9:
                    numBlanks += 1
            if i.number == numBlanks:
                for y in i.surrounding:
                    if y.number == 9:
                        toDelete.append(y)
                        y.mine = True

        return list(set(toDelete))

    def leftClickList(self, toClick):
        for mine in toClick:
            if not mine.mine and not mine.hasBeenLeftClicked:
                #time.sleep(.1)
                pag.moveTo(mine.screenPosition[0], mine.screenPosition[1], CLICK_DELAY)
                pag.click()
                mine.hasBeenLeftClicked = True


    def rightClickList(self, toClick):
        if toClick is not None:
            for mine in toClick:
                if not mine.flagged:
                    #time.sleep(.1)
                    pag.moveTo(mine.screenPosition[0], mine.screenPosition[1], CLICK_DELAY)
                    pag.rightClick()
                    mine.flagged = True

    def checkEasyMines(self):
        toClick = []
        for i in self.tiles:
            numMines = 0
            for j in i.surrounding:
                if j.mine:
                    numMines += 1
            if i.number == numMines:
                for y in i.surrounding:
                    if y.number == 9:
                        toClick.append(y)

        return list(set(toClick))

    def firstClick(self):
        while True:
            numBlanks = 0
            for i in self.tiles:
                if i.number == 0:
                    numBlanks += 1
            if numBlanks < 5:
                pag.click(self.board.topLeft[0] + random.randint(10, 180),
                      self.board.topLeft[1] + random.randint(10, 180))
                self.board.scanTiles()
            else:
                break

    def checkOneTwoOne(self):
        twos = []
        for i in self.tiles:
            if i.number == 2:
                twos.append(i)
        vertical = []
        horizontal = []
        try:
            for i in twos:
                # 1,6 3,4
                if (i.surrounding[1].number == 1 and i.surrounding[6].number == 1):
                    vertical.append(i)
                elif i.surrounding[3].number == 1 and i.surrounding[4].number == 1:
                    horizontal.append(i)
            toClick = []
            for i in vertical:
                if i.surrounding[0].number == 9 and i.surrounding[5].number == 9:
                    toClick.append(i.surrounding[0])
                    toClick.append(i.surrounding[5])
                # make this more specific
                else:
                    toClick.append(i.surrounding[2])
                    toClick.append(i.surrounding[7])
            for i in horizontal:
                if i.surrounding[0].number == 9 and i.surrounding[2].number == 9:
                    toClick.append(i.surrounding[0])
                    toClick.append(i.surrounding[2])
                # make this more specific
                else:
                    toClick.append(i.surrounding[5])
                    toClick.append(i.surrounding[7])
            return list(set(toClick))
        except IndexError as err:
            print("Index on edge case 121 {}".format(err))
