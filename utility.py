import const

def checkRow(row):
    if row < 0 or row >= const.ROWS:
        raise ValueError("Bad row value")

def checkCol(col):
    if col < 0 or col >= const.COLUMNS:
        raise ValueError("Bad column value")


def getRow( char ):
    return int(chr(ord(char)-( ord('a')-ord('0') )))

def getCol( char ):
    return int(char)-1


def sign( expression ):
    if expression > 0:
        return 1
    elif expression < 0:
        return -1
    else:
        return 0
