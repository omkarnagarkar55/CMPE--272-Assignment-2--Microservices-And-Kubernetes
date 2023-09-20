from flask import Flask, jsonify, request, abort
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

# Database configuration
DB_HOST = "database"  # Name of the PostgreSQL service in Kubernetes
DB_PORT = 5432
DB_USER = "postgres"
DB_PASSWORD = "password"  # This should be fetched securely, e.g., from environment variables or Kubernetes secrets
DB_NAME = "flaskblog"

def get_db_connection():
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    return conn

@app.route('/posts', methods=['GET'])
def get_posts():
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute('SELECT * FROM posts')
    posts = cursor.fetchall()
    conn.close()
    return jsonify(posts)

@app.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute('SELECT * FROM posts WHERE id = %s', (post_id,))
    post = cursor.fetchone()
    conn.close()
    if not post:
        abort(404)
    return jsonify(post)

@app.route('/posts', methods=['POST'])
def create_post():
    if not request.json or not 'title' in request.json or not 'content' in request.json:
        abort(400)
    title = request.json['title']
    content = request.json['content']
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute('INSERT INTO posts (title, content) VALUES (%s, %s) RETURNING id', (title, content))
    post_id = cursor.fetchone()['id']
    conn.commit()
    conn.close()
    return jsonify({'id': post_id}), 201

@app.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    if not request.json:
        abort(400)
    title = request.json.get('title', "")
    content = request.json.get('content', "")
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute('UPDATE posts SET title = %s, content = %s WHERE id = %s', (title, content, post_id))
    conn.commit()
    conn.close()
    return jsonify({'result': 'success'})

@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute('DELETE FROM posts WHERE id = %s', (post_id,))
    conn.commit()
    conn.close()
    return jsonify({'result': 'success'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
