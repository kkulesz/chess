#!/usr/local/bin/python3

import board
import figures
import const
import utility

class BoardManager:
    def __init__(self, file_name=None):
        #white starts, if game is read from file, then it will get overwrited
        self.__turn = const.WHITE
        if file_name is None:
            self.__board = board.Board()

            self.__initPlayer( const.WHITE )
            self.__initPlayer( const.BLACK )
        else:
            self.__readFromFile(file_name)

    def __readFromFile(self,file_name):
        if len(file_name) < 1 :
            raise ValueError("File name")
        
        self.__board = board.Board()
        board_file = open(file_name, "r")
        for i in range( const.ROWS):
            row = board_file.readline()
            col = 0
            for j in range(0,len(row)-1,4 ):
                if row[j+2] == 'b':
                    color = const.WHITE
                elif row[j+2] == 'c':
                    color = const.BLACK

                if row[j+1] == 'i':
                    self.__board.setFigure( figures.Pawn(color), i, col)
                elif row[j+1] == 'r':
                    self.__board.setFigure( figures.Rook(color), i, col)
                elif row[j+1] == 'k':
                    self.__board.setFigure( figures.Knight(color), i, col)
                elif row[j+1] == 'b':
                    self.__board.setFigure( figures.Bishop(color), i, col)
                elif row[j+1] == 'Q':
                    self.__board.setFigure( figures.Queen(color), i, col)
                elif row[j+1] == 'K':
                    self.__board.setFigure( figures.King(color), i, col)

                col+=1

        whose_turn = board_file.readline()
        if whose_turn == "WHITE\n":
            self.__turn = const.WHITE
        elif whose_turn == "BLACK\n":
            self.__turn = const.BLACK




    def saveToFile(self, file_name):
        if len(file_name) < 1 :
            raise ValueError("File name")

        boards_to_save = []
        for i in range(const.ROWS):
            row = "" 
            for j in range(const.COLUMNS):
                row += self.__board.getFieldState(i, j)
            boards_to_save.append(row)
        
        
        board_file = open(file_name, 'w')
        for i in boards_to_save:
            board_file.write(i+'\n')

        if self.__turn == const.WHITE:
            board_file.write("WHITE")
        elif self.__turn == const.BLACK:
            board_file.write("BLACK")
        board_file.write('\n')
        board_file.close()


    def __initPlayer(self, color):
        if color == const.WHITE:
            first_row = 1
            second_row = 0
        elif color == const.BLACK:
            first_row = 6
            second_row = 7
        else:
            raise ValueError("Player can be either black or white")

        for i in range(const.PAWNS):
            self.__board.setFigure( figures.Pawn(color), first_row, i)

        self.__board.setFigure( figures.Rook(color), second_row, 0)
        self.__board.setFigure( figures.Rook(color), second_row, 7)

        self.__board.setFigure( figures.Knight(color), second_row, 1)
        self.__board.setFigure( figures.Knight(color), second_row, 6)

        self.__board.setFigure( figures.Bishop(color), second_row, 2)
        self.__board.setFigure( figures.Bishop(color), second_row, 5)

        self.__board.setFigure( figures.Queen(color), second_row, 4)
        self.__board.setFigure( figures.King(color), second_row, 3)

    def changeTurn(self):
        self.__turn = (self.__turn+1)%2

    def getTurn(self):
        return self.__turn

    #check whether it is vertical move
    #and whether fields between are empty
    def __verticalMove(self, src_row, src_col, dest_row, dest_col):
        if abs(src_row-dest_row) == 0 and abs(src_col-dest_col) != 0:
            for i in range(src_col, dest_col):
                if i != src_col and i != dest_col and not self.__board.isFree(src_row, i):
                    return False

        elif abs(src_row-dest_row) != 0 and abs(src_col-dest_col) == 0:
            for i in range(src_row, dest_row):
                if i != src_row and i != dest_row and not self.__board.isFree(i, src_col):
                    return False

        else:
            return False

        return True

    #check whether it is cross move
    #and whether fields between are empty
    def __crossMove(self, src_row, src_col, dest_row, dest_col):
        if abs(src_row-dest_row) == abs(src_col-dest_col) != 0:
            pass
        else:
            return False

        row_diff = src_row-dest_row
        col_diff = src_col-dest_col

        y_sign = utility.sign(dest_row-src_row) 
        x_sign = utility.sign(dest_col-src_col)
        for i in range( 1, abs(dest_row-src_row) ):
            if not self.__board.isFree( i*y_sign+src_row, i*x_sign+src_col) and i*y_sign+src_row != dest_row:
                #print( str(i*y_sign+src_row) + ":" + str(i*x_sign+src_col))
                return False

        return True

    def __isPawnMovePossible(self, src_row, src_col, dest_row, dest_col):
        if self.__turn == const.WHITE:
            direction = 1
        elif self.__turn == const.BLACK:
            direction = -1
        else:
            raise ValueError("Just black and white player")

        if (src_row + direction == dest_row) and (src_col == dest_col) and self.__board.isFree(dest_row, dest_col):
            return True
        elif (src_row + direction == dest_row) and abs(src_col-dest_col)==1 and not self.__board.isFree(dest_row, dest_col):
            return True
        elif (self.__board.getFigure(src_row, src_col).firstMoveAvailable() ) and (src_row + 2*direction == dest_row) and (src_col == dest_col) and self.__board.isFree(dest_row, dest_col):
            self.__board.getFigure(src_row, src_col).move()
            return True

        return False


    def __isRookMovePossible(self, src_row, src_col, dest_row, dest_col):
        return self.__verticalMove(src_row, src_col, dest_row, dest_col)

    def __isKnightMovePossible(self, src_row, src_col, dest_row, dest_col):
        if abs(src_row-dest_row)==1 and abs(src_col-dest_col)==2:
            return True
        elif abs(src_row-dest_row)==2 and abs(src_col-dest_col)==1:
            return True
        
        return False
        
    def __isBishopMovePossible(self, src_row, src_col, dest_row, dest_col):
        return self.__crossMove(src_row, src_col, dest_row, dest_col)

    def __isQueenMovePossible(self, src_row, src_col, dest_row, dest_col):
        #XOR on crossMove and verticalMove
        return (self.__crossMove(src_row,src_col, dest_row,dest_col) ^ self.__verticalMove(src_row, src_col, dest_row, dest_col))

    def __isKingMovePossible(self, src_row, src_col, dest_row, dest_col):
        if abs(src_row-dest_row)==1 and abs(src_col-dest_col)==0:
            return True
        elif abs(src_row-dest_row)==0 and abs(src_col-dest_col)==1:
            return True
        elif abs(src_row-dest_row)==1 and abs(src_col-dest_col)==1:
            return True
        else:
            return False

    def __isMovePossible(self, src_row, src_col, dest_row, dest_col):
        #utility.checkRow(src_row)
        #utility.checkCol(src_col)

        #utility.checkRow(dest_row)
        #utility.checkCol(dest_col)

        src_color = self.__board.getFigureColor(src_row, src_col)
        dest_color = self.__board.getFigureColor(dest_row, dest_col)


        if src_color != self.__turn:
            return False
        if src_color == dest_color:
            return False
        
        figure = self.__board.getFigure(src_row, src_col)
        if( type(figure) == type( figures.Pawn()) ):
            if not self.__isPawnMovePossible(src_row, src_col, dest_row, dest_col):
                return False

        elif type(figure) == type( figures.Rook() ):
            if not self.__isRookMovePossible(src_row, src_col,dest_row, dest_col):
                return False

        elif type(figure) == type( figures.Knight() ):
            if not self.__isKnightMovePossible(src_row, src_col,dest_row, dest_col):
                return False

        elif type(figure) == type( figures.Bishop() ):
            if not self.__isBishopMovePossible(src_row, src_col,dest_row, dest_col):
                return False 

        elif type(figure) == type( figures.Queen() ):
            if not self.__isQueenMovePossible(src_row, src_col,dest_row, dest_col):
                return False

        elif type(figure) == type( figures.King() ):
            if not self.__isKingMovePossible(src_row, src_col,dest_row, dest_col):
                return False
         
        return True

    def moveFigure(self, src, dest):
        src_row = utility.getRow(src[0]) 
        src_col = utility.getCol(src[1])

        dest_row = utility.getRow(dest[0])
        dest_col = utility.getCol(dest[1])

        if not self.__isMovePossible( src_row, src_col, dest_row, dest_col):
           return False
               
        figure = self.__board.removeFigure(src_row, src_col)
        self.__board.setFigure(figure, dest_row,dest_col)
        return True

    def getBoardState(self):
        return self.__board.getState()
