from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/easy')
def easy_mode():
    return render_template('board.html', show_products=True)


@app.route('/hard')
def hard_mode():
    return render_template('board.html', show_products=False)


if __name__ == '__main__':
    app.run(debug=True)
