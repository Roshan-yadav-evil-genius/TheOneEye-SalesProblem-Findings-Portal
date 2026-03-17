from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

USER_DATA_FILE = 'user_data.json'


def load_problems():
    problems = []
    with open('problems.jsonl', 'r') as f:
        for line in f:
            if line.strip():
                problems.append(json.loads(line))
    return problems


def load_user_data():
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, 'r') as f:
            return json.load(f)
    return {}


def save_user_data(data):
    with open(USER_DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/problems')
def api_problems():
    problems = load_problems()
    user_data = load_user_data()
    for p in problems:
        slug = p.get('proposed_slug', '')
        ud = user_data.get(slug, {})
        p['status'] = ud.get('status', 'raw')
        p['notes'] = ud.get('notes', '')
    return jsonify(problems)


@app.route('/api/status', methods=['POST'])
def api_status():
    body = request.get_json()
    slug = body.get('slug')
    status = body.get('status')
    if not slug or status not in ('raw', 'done', 'review', 'todo', 'deleted'):
        return jsonify({'error': 'Invalid slug or status'}), 400
    user_data = load_user_data()
    user_data.setdefault(slug, {})['status'] = status
    save_user_data(user_data)
    return jsonify({'ok': True})


@app.route('/api/notes', methods=['POST'])
def api_notes():
    body = request.get_json()
    slug = body.get('slug')
    notes = body.get('notes', '')
    if not slug:
        return jsonify({'error': 'Invalid slug'}), 400
    user_data = load_user_data()
    user_data.setdefault(slug, {})['notes'] = notes
    save_user_data(user_data)
    return jsonify({'ok': True})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
