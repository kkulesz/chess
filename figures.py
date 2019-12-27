#!/usr/local/bin/python3

import const

class Figure:
    def __init__(self, color=const.NO_COLOR):
        self._sign = "x"
        self._color = color

    def getColor(self):
        return self._color
    def getSign(self):
        return self._sign

class Pawn(Figure):
    def __init__(self, color=const.NO_COLOR):
        self.__first_move = True
        self._sign = "i"
        self._color = color

    def move(self):
        self.__first_move = False
    def firstMoveAvailable(self):
        return self.__first_move

class Rook(Figure):
    def __init__(self, color=const.NO_COLOR):
        self._sign = "r"
        self._color = color

class Knight(Figure):
    def __init__(self, color=const.NO_COLOR):
        self._sign = "k"
        self._color = color    

class Bishop(Figure):
    def __init__(self, color=const.NO_COLOR):
        self._sign = "b"
        self._color = color

class Queen(Figure):
    def __init__(self, color=const.NO_COLOR):
        self._sign = "Q"
        self._color = color

class King(Figure):
    def __init__(self, color=const.NO_COLOR):
        self._sign = "K"
        self._color = color



class FiguresSet:
    def __init__(self, color):
       self.__pawns = []
       for i in range(const.PAWNS):
           self.__pawns.append( Pawn(color) )
