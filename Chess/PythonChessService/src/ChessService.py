import flask
from chessutil.validationutil import ChessValidationUtil

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/computer/move', methods=['POST'])
def computerMove():
    validMoves = ChessValidationUtil.determineValidMoves(flask.request.json['color'], flask.request.json['position'])
    return validMoves

app.run()