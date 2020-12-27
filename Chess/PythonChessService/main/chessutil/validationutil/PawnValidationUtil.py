from main.chessutil.validationutil.Constants import BOARD_X_POS

def getValidPawnMoves(color, key, json):
    print("Getting valid moves for Pawn at "+key)


def canCapture(color, key, json):
    x = BOARD_X_POS.find(key[0])
    x1 = BOARD_X_POS[x + 1]
    x2 = BOARD_X_POS[x - 1]
    y = int(key[1])
    cells = []
    captures = []
    if color == 'w':
        cells.append(x1+str(y + 1))
        cells.append(x2+str(y + 1))
    elif color == 'b':
        cells.append(x1+str(y - 1))
        cells.append(x2+str(y - 1))
    for cell in cells:
        if cell in json and not json[cell].startswith(color):
            captures.append(cell)
    return captures

def canEnPassant():
    return False

