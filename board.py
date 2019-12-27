#!/usr/local/bin/python3

import figures
import const
import utility

class Board:
    class Field:
        def __init__(self, figure=None):
            self.__figure = figure

        def removeFigure(self):
            old = self.__figure
            self.__figure = None
            return old

        def getFigure(self):
            return self.__figure

        def getFigureColor(self):
            if self.isFree():
                return const.NO_COLOR
            else :
                return self.__figure.getColor()

        def setFigure(self, figure):
            old = self.getFigure()
            self.__figure = figure
            return old

        def isFree(self):
            if self.__figure is None:
                return True
            else:
                return False

        def getFieldState(self):
            state = "["
            if self.isFree():
                state+= "  "
            else:
                state += self.__figure.getSign()

            if self.getFigureColor() == const.WHITE:
                state += "b"
            elif self.getFigureColor() == const.BLACK:
                state += "c"
            state+= "]"
            return state
    ##############Field###############

    def __init__(self):
        self.__fields = []
        for i in range(const.ROWS):
            row = []
            self.__fields.append(row)
            for j in range(const.COLUMNS):
                self.__fields[i].append( self.Field() )

    def isFree(self, row, col):
        #utility.checkRow(row)
        #utility.checkCol(col)
        return self.__fields[row][col].isFree()

    def removeFigure(self, row, col):
        #utility.checkRow(row)
        #utility.checkCol(col)
        return self.__fields[row][col].removeFigure()

    def getFigure(self, row, col):
        #utility.checkRow(row)
        #utility.checkCol(col)
        return self.__fields[row][col].getFigure()

    def getFigureColor(self, row, col):
        return self.__fields[row][col].getFigureColor()

    def setFigure(self, figure, row, col):
        #utility.checkRow(row)
        #utility.checkCol(col)
        return self.__fields[row][col].setFigure(figure)

    def getFieldState(self, row, col):
        return self.__fields[row][col].getFieldState()

    def getState(self):
        row = 'a'
        state = "  1   2   3   4   5   6   7   8\n"
        for i in range( const.ROWS ):
            state += row
            for j in range( const.COLUMNS ):
                state += self.__fields[i][j].getFieldState()
            state+="\n"
            row = chr( ord( row) + 1)

        return state


if __name__ == "__main__":
    pass
