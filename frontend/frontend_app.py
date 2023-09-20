from flask import Flask, render_template, request, url_for, flash, redirect
import requests  # To make API calls

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'
POSTS_SERVICE_URL = 'http://posts-service:5000'  # Assuming the Posts Service is named 'posts-service' in Kubernetes

@app.route('/')
def index():
    response = requests.get(f'{POSTS_SERVICE_URL}/posts')
    posts = response.json()
    return render_template('index.html', posts=posts)

@app.route('/<int:post_id>')
def post(post_id):
    response = requests.get(f'{POSTS_SERVICE_URL}/posts/{post_id}')
    post = response.json()
    return render_template('post.html', post=post)

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            data = {'title': title, 'content': content}
            response = requests.post(f'{POSTS_SERVICE_URL}/posts', json=data)
            if response.status_code == 201:
                return redirect(url_for('index'))
            else:
                flash('There was an error creating the post.')

    return render_template('create.html')

@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    response = requests.get(f'{POSTS_SERVICE_URL}/posts/{id}')
    post = response.json()

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            data = {'title': title, 'content': content}
            response = requests.put(f'{POSTS_SERVICE_URL}/posts/{id}', json=data)
            if response.status_code == 200:
                return redirect(url_for('index'))
            else:
                flash('There was an error updating the post.')

    return render_template('edit.html', post=post)

@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    response = requests.delete(f'{POSTS_SERVICE_URL}/posts/{id}')
    if response.status_code == 200:
        flash('Post was successfully deleted!')
    else:
        flash('There was an error deleting the post.')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
