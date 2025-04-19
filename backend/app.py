from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

# Initialize SQLite database (for demonstration purposes)
DATABASE = 'users.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Return rows as dictionaries
    return conn

def init_db():
    with app.app_context():
        db = get_db()
        with open('schema.sql', 'r') as f:
            db.cursor().executescript(f.read())
        db.commit()

# Create the database schema if it doesn't exist
with app.app_context():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
    if cursor.fetchone() is None:
        init_db()

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({"message": "Data from the backend!"})

@app.route('/api/users', methods=['GET'])
def get_user():
    username = request.args.get('username')
    if not username:
        return jsonify({"error": "Username parameter is required"}), 400

    db = get_db()
    cursor = db.cursor()
    # Vulnerable SQL query - DO NOT USE THIS IN PRODUCTION
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    user = cursor.fetchone()
    db.close()

    if user:
        return jsonify(dict(user))
    else:
        return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
