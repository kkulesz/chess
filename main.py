#!/usr/local/bin/python3

import board_manager
import text_interface

def main():
    interface = text_interface.TextInterface()
    interface.mainMenu()
if __name__ == "__main__":
    main()
