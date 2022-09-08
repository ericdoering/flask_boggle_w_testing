from boggle import Boggle
from flask import Flask, request, render_template, jsonify, session

app = Flask(__name__)
app.config["SECRET-KEY"] = "pythonpelican1997$"


boggle_game = Boggle()


@app.route("/")
def home_page():
    """brings user to starting homepage"""
    board = boggle_game.make_board()
    session["board"] = board
    highscore = session.get("highscore", 0)
    numplays = session.get("numplays", 0)

    return render_template("index.html", board=board, highscore=highscore, numplays=numplays)



@app.route("/check-word")
def check_word():
    """checks to see if the word is the dictionary"""
    word = request.args["word"]
    board = session["board"]
    response = boggle_game.check_valid_word(board, word)

    return jsonify({"result": response})



@app.route("/post-score", methods=["POST"])
def render_score():
    """Renders game score"""
    score = request.json["score"]
    highscore = session.get("highscore", 0)
    numplays = session.get("numplays", 0)

    session["numplays"] = numplays + 1
    session["highscore"] = max(score, highscore)

    return jsonify(brokeRecord=score > highscore)