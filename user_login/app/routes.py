from flask import redirect, render_template, url_for
from forms import LoginForm
from app import app

@app.route('/')
@app.route('/index')
def index():
    username = 'Ries'
    post = [{'username': 'test'}]
    return render_template('index.html', username=username, post=post)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', form=from, title='Sign Ip')

@app.route('/logout')
def logout():
    pass