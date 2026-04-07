from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

USER_DATA_FILE = 'user_data.json'
INNOVATIONS_FILE = 'innovations.jsonl'


def load_problems():
    problems = []
    with open('problems.jsonl', 'r') as f:
        for line_num, line in enumerate(f, start=1):
            if line.strip():
                p = json.loads(line)
                p['line_id'] = line_num
                p['slug'] = f'problem:{line_num}'
                problems.append(p)
    return problems


def load_innovations():
    if not os.path.exists(INNOVATIONS_FILE):
        return []
    items = []
    with open(INNOVATIONS_FILE, 'r') as f:
        for line_num, line in enumerate(f, start=1):
            if line.strip():
                row = json.loads(line)
                row['line_id'] = line_num
                row['slug'] = f'innovation:{line_num}'
                items.append(row)
    return items


def load_user_data():
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, 'r') as f:
            return json.load(f)
    return {}


def save_user_data(data):
    with open(USER_DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/problems')
def problems_page():
    return render_template('problems.html')


@app.route('/innovations')
def innovations_page():
    return render_template('innovations.html')


@app.route('/api/problems')
def api_problems():
    problems = load_problems()
    user_data = load_user_data()
    for p in problems:
        new_slug = p['slug']
        old_key = p.get('proposed_slug', '')
        if new_slug in user_data:
            ud = user_data[new_slug]
        elif old_key in user_data:
            ud = user_data[old_key]
        else:
            ud = {}
        p['status'] = ud.get('status', 'raw')
        p['notes'] = ud.get('notes', '')
    return jsonify(problems)


@app.route('/api/innovations')
def api_innovations():
    items = load_innovations()
    user_data = load_user_data()
    for row in items:
        slug = row['slug']
        ud = user_data.get(slug, {})
        row['status'] = ud.get('status', 'raw')
        row['notes'] = ud.get('notes', '')
    return jsonify(items)


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
    app.run(debug=True, port=5000, host='0.0.0.0')
