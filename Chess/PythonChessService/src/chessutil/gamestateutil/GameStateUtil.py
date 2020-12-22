__moves = []

class Move():
    def __init__(self, moveFrom, moveTo):
        self.moveFrom = moveFrom
        self.moveTo = moveTo

def getLastMove():
    return __moves[-1]

def addMove(move : Move):
    __moves.append(move)


def undoLastMove():
    __moves.pop()
