# Multiplication Bingo

This repository contains a simple script that generates and displays a Bingo board in the console and a small Flask web app that shows a 12x12 grid. The web page also generates a random number between 1 and 144 each time you click the "Next Number" button.

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

3. Open <http://localhost:5000/> in a web browser to view the board. Click "Next Number" to draw a new random number on the page.

For deployment, host the app on any platform that supports Flask applications (Heroku, Fly.io, etc.) and ensure the environment installs the dependency and runs `python3 app.py` or uses a production server like Gunicorn.
