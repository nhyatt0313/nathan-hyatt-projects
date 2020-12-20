from chessutil.validationutil.__Constants import BOARD_X_POS

def getValidKingMoves(color, key, json):
    print("Getting valid moves for King at "+key)
    x = BOARD_X_POS.find(key[0])
    y = int(key[1])
    allKeys = [f'{BOARD_X_POS[x - 1]}{str(y - 1)}',
               f'{BOARD_X_POS[x - 1]}{str(y)}',
               f'{BOARD_X_POS[x - 1]}{str(y + 1)}',
               f'{BOARD_X_POS[x]}{str(y + 1)}',
               f'{BOARD_X_POS[x + 1]}{str(y + 1)}',
               f'{BOARD_X_POS[x + 1]}{str(y)}',
               f'{BOARD_X_POS[x + 1]}{str(y - 1)}',
               f'{BOARD_X_POS[x]}{str(y - 1)}']
    print("all keys: "+str(allKeys))
    allBoardKeys = [k for k in allKeys if '|' not in k and '0' not in k and '9' not in k]
    print("all board keys: "+str(allBoardKeys))
    print("color: "+color)
    allValidKeys = [k for k in allBoardKeys if k not in json or not json[k].startswith(color)]
    for i, k in enumerate(allValidKeys):
        if k in json:
            allValidKeys[i] = 'x'+k
    print("all valid keys: "+str(allValidKeys))
    return allValidKeys