from flask import Flask, render_template
import random

app = Flask(__name__)


def generate_bingo_board():
    ranges = {
        'B': range(1, 16),
        'I': range(16, 31),
        'N': range(31, 46),
        'G': range(46, 61),
        'O': range(61, 76)
    }
    board = [random.sample(ranges[letter], 5) for letter in 'BINGO']
    board[2][2] = 'FREE'
    return board


@app.route('/')
def index():
    board = generate_bingo_board()
    return render_template('board.html', board=board)


if __name__ == '__main__':
    app.run(debug=True)
