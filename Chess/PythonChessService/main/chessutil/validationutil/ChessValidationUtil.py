from main.chessutil.validationutil import KingValidationUtil
from main.chessutil.validationutil import QueenValidationUtil
from main.chessutil.validationutil import RookValidationUtil
from main.chessutil.validationutil import BishopValidationUtil
from main.chessutil.validationutil import KnightValidationUtil
from main.chessutil.validationutil import PawnValidationUtil


def __getValidMoves(key, value, json): 
    if value.endswith('K'): ## KING
        return KingValidationUtil.getValidKingMoves(value[0], key, json)
    if value.endswith('Q'): ## QUEEN
        return QueenValidationUtil.getValidQueenMoves(value[0], key, json)
    if value.endswith('R'): ## ROOK   
        return RookValidationUtil.getValidRookMoves(value[0], key, json)
    if value.endswith('B'): ## BISHOP 
        return BishopValidationUtil.getValidBishopMoves(value[0], key, json)
    if value.endswith('N'): ## KNIGHT 
        return KnightValidationUtil.getValidKnightMoves(value[0], key, json)
    if value.endswith('P'): ## PAWN 
        return PawnValidationUtil.getValidPawnMoves(value[0], key, json)
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

