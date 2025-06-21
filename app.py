from flask import Flask, render_template, request, jsonify
import json
import os

# Determine the path to the scores file relative to this script so that the app
# works no matter where it's launched from.
SCORE_FILE = os.path.join(os.path.dirname(__file__), 'scores.json')


def load_scores(path=SCORE_FILE):
    """Load the score data from disk."""
    if not os.path.exists(path):
        return {"fastest": [], "fewest": []}
    with open(path, 'r') as f:
        return json.load(f)


def save_scores(data, path=SCORE_FILE):
    """Persist the score data to disk."""
    with open(path, 'w') as f:
        json.dump(data, f)


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


def format_time(seconds):
    minutes = seconds // 60
    secs = seconds % 60
    return f"{minutes}:{secs:02d}"


@app.route('/leaderboard')
def leaderboard():
    scores = load_scores()
    fastest = sorted(
        scores.get('fastest', []),
        key=lambda x: x['time'],
    )[:20]
    for entry in fastest:
        entry['formatted_time'] = format_time(entry['time'])
    fewest = sorted(
        scores.get('fewest', []),
        key=lambda x: x['count'],
    )[:20]
    return render_template(
        'leaderboard.html',
        fastest=fastest,
        fewest=fewest,
    )


@app.route('/easy')
def easy_mode():
    return render_template('board.html', show_products=True)


@app.route('/hard')
def hard_mode():
    return render_template('board.html', show_products=False)


@app.route('/check_score')
def check_score():
    try:
        time = int(request.args.get('time', 0))
        count = int(request.args.get('count', 0))
    except (TypeError, ValueError):
        return jsonify({'fastest': False, 'fewest': False})

    scores = load_scores()
    fast = scores.get('fastest', [])
    few = scores.get('fewest', [])
    qualifies_fast = (
        len(fast) < 20
        or time < max(fast, key=lambda x: x['time'])['time']
    )
    qualifies_few = (
        len(few) < 20
        or count < max(few, key=lambda x: x['count'])['count']
    )
    return jsonify({'fastest': qualifies_fast, 'fewest': qualifies_few})


@app.route('/submit_score', methods=['POST'])
def submit_score():
    data = request.get_json(force=True)
    name = data.get('name', 'Anonymous')[:20]
    time = int(data.get('time', 0))
    count = int(data.get('count', 0))

    scores = load_scores()
    fast = scores.setdefault('fastest', [])
    few = scores.setdefault('fewest', [])

    if (
        len(fast) < 20
        or time < max(fast, key=lambda x: x['time'])['time']
    ):
        if len(fast) >= 20:
            fast.remove(max(fast, key=lambda x: x['time']))
        fast.append({'name': name, 'time': time})

    if (
        len(few) < 20
        or count < max(few, key=lambda x: x['count'])['count']
    ):
        if len(few) >= 20:
            few.remove(max(few, key=lambda x: x['count']))
        few.append({'name': name, 'count': count})

    save_scores(scores)
    return jsonify({'success': True})


if __name__ == '__main__':
    app.run(debug=True)
