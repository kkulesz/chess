import os
import board_manager
import const


class TextInterface:
    def __init__(self):
        self.__manager = board_manager.BoardManager()

    def __userMoveInput(self):
        return input("Enter move: ")

    def __userMenuInput(self):
        return input("Enter option: ")

    def __printWhoseTurn(self):
        print("============", end="")
        if self.__manager.getTurn() == const.WHITE:
            print("Biały",end="")
        elif self.__manager.getTurn() == const.BLACK:
            print("Czarny",end="")
        else:
            raise ValueError("Turn problem")
        print("============")

    def __checkFieldCoordinate(self, x):
        if ord(x[0]) < ord('a') or ord(x[0]) > ord('h'):
            return False
        if ord(x[1]) < ord('1') or ord(x[1]) > ord('8'):
            return False
        return True

    def __checkMoveInput(self, move):
        if len(move) != 5:
            return False

        if not self.__checkFieldCoordinate(move[0:2]) or not self.__checkFieldCoordinate(move[3:5]):
            return False
        if move[2] != ' ' and move[2] != ':' and move[2] != '-':
            return False
        return True

    
    def __printMainMenu(self):
        print("Welcome to chess!")
        print("[1]Play")
        print("[2]Load")
        print("[3]How_to")
        print("[0]Leave")

    def __printHowTo(self):
       how_to = open("files/howTo.txt", 'r')
       print( how_to.read())

    def mainMenu(self):
        while True:
            self.__printMainMenu()
            option = int(self.__userMenuInput())
            if option == 1:
                self.__gameLoop()
            elif option == 2:
                self.__manager = board_manager.BoardManager("save.txt")
                self.__gameLoop()
            elif option == 3:
                self.__printHowTo()
            elif option == 0:
                print("Bye!")
                return

    def __gameLoop(self):
        print(self.__manager.getBoardState())

        while True:
            self.__printWhoseTurn()
            move = self.__userMoveInput()
            if move == "save":
                self.__manager.saveToFile("files/save.txt")
                print("GAME SAVED!")
                continue
            if not self.__checkMoveInput(move):
                print("Bad format, try again")
                continue
            src = move[0:2]
            dest = move[3:5]
            if not self.__manager.moveFigure(src, dest):
                print("Bad move, try again")
                continue

            self.__manager.changeTurn()  

            #works only for unix, 'cls' for windows
            os.system('clear')

            print(self.__manager.getBoardState())
