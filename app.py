from flask import Flask, render_template

app = Flask(__name__)

def generate_board():
    """Return a 12x12 grid with sequential numbers 1..144."""
    board = []
    num = 1
    for _ in range(12):
        row = list(range(num, num + 12))
        board.append(row)
        num += 12
    return board


@app.route('/')
def index():
    board = generate_board()
    return render_template('board.html', board=board)


if __name__ == '__main__':
    app.run(debug=True)
