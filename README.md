# Multiplication Bingo

This repository contains a command-line script that prints a 12x12 multiplication table and a small Flask web app that displays the same table in the browser. The web page generates a random number between 1 and 144, and a new one is drawn whenever you correctly select the matching product on the board. When you get a match, the message "Correct!" stays on screen for a few seconds before the next number shows up.

To win the bingo game you must mark a complete line of twelve correct cells in a row, horizontally, vertically or diagonally.

The board page also shows a stopwatch in the upper left corner so you can see how long it takes to win. The timer starts when the board loads and stops once you hit Bingo.

## Command-line usage

```bash
python3 bingo_board.py
```

## Web app usage

1. Verify that Python is installed (e.g. `python --version` or `python3 --version`):

```bash
python3 --version
```

2. Install the requirements:

```bash
python3 -m pip install -r requirements.txt
```

3. Run the Flask app:

```bash
python3 app.py
```

4. Open <http://localhost:5000/> in a web browser. You'll be greeted with a welcome screen offering "Easy" or "Hard" mode. Easy mode shows the multiplication products on the bingo board while Hard mode leaves the squares blank.

For deployment, host the app on any platform that supports Flask applications (Heroku, Fly.io, etc.) and ensure the environment installs the dependency and runs `python3 app.py` or uses a production server like Gunicorn.
