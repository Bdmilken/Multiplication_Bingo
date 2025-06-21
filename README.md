# Multiplication Bingo

This repository contains a command-line script that prints a 12x12 multiplication table and a small Flask web app that displays the same table in the browser. The web page generates a random number between 1 and 144, and a new one is drawn whenever you correctly select the matching product on the board. When you get a match, the message "Correct!" stays on screen for a few seconds before the next number shows up.

To win the bingo game you must mark a complete line of twelve correct cells in a row, horizontally, vertically or diagonally.

The board page also shows a stopwatch in the upper left corner so you can see how long it takes to win. The timer starts when the board loads and stops once you hit Bingo.
A counter below the timer tracks how many squares you've correctly identified and shows the final total when the game ends.

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
5. Navigate to <http://localhost:5000/leaderboard> to view the fastest times and fewest squares used. Scores are stored in `scores.json` (an example file lives in the `example/` directory).

For deployment, host the app on any platform that supports Flask applications (Heroku, Fly.io, etc.) and ensure the environment installs the dependency and runs `python3 app.py` or uses a production server like Gunicorn.

## License

This project is licensed under the [MIT License](LICENSE).
## Docker usage

To run the app inside a container you can use the provided Dockerfile. Build and start the container with:

```bash
docker build -t multiplication-bingo .
docker run -p 8080:8080 multiplication-bingo
```

Gunicorn is installed via `requirements.txt` and the container listens on port 8080.
When deploying in production, mount persistent storage (for example a Fly.io volume or a database) so the `scores.json` file is preserved across deployments.

### Persisting scores

To keep leaderboard data when the container restarts, mount `scores.json` on a
persistent volume. Create a volume and attach it when starting the container:

```bash
docker volume create bingo-scores
docker run -p 8080:8080 -v bingo-scores:/app/scores.json multiplication-bingo
```

You can also mount a local file instead of a Docker volume:

```bash
docker run -p 8080:8080 \
  -v "$(pwd)/scores.json:/app/scores.json" multiplication-bingo
```

Use the same volume or file every time you launch the container so the saved
results persist between runs.
