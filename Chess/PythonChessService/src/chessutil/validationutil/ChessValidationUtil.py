from chessutil.validationutil import __KingValidationUtil
from chessutil.validationutil import __QueenValidationUtil
from chessutil.validationutil import __RookValidationUtil
from chessutil.validationutil import __BishopValidationUtil
from chessutil.validationutil import __KnightValidationUtil
from chessutil.validationutil import __PawnValidationUtil


def __getValidMoves(key, value, json): 
    if value.endswith('K'): ## KING
        return __KingValidationUtil.getValidKingMoves(value[0], key, json)
    if value.endswith('Q'): ## QUEEN
        return __QueenValidationUtil.getValidQueenMoves(value[0], key, json)
    if value.endswith('R'): ## ROOK   
        return __RookValidationUtil.getValidRookMoves(value[0], key, json)
    if value.endswith('B'): ## BISHOP 
        return __BishopValidationUtil.getValidBishopMoves(value[0], key, json)
    if value.endswith('N'): ## KNIGHT 
        return __KnightValidationUtil.getValidKnightMoves(value[0], key, json)
    if value.endswith('P'): ## PAWN 
        return __PawnValidationUtil.getValidPawnMoves(value[0], key, json)
    print("ERROR: Invalid peice code in ChessValidationUtil.__getValidMoves")
    return []



def determineValidMoves(color, json):
    validMoves = {}
    for key, value in json.items():
        print("Key: "+key)
        print("Value: "+value)
        if value.startswith(color):
            validMoves[key] = __getValidMoves(key, value, json)
    return validMoves

