from flask import Flask
from markupsafe import escape
from flask import url_for

app = Flask(__name__)


@app.route('/user/<name>')
def user_page(name):
    return f'User: {escape(name)}'


@app.route('/')
def hello():
    return "Hello!"


@app.route('/test')
def test_url_for():
    return url_for('user_page', name='peter')