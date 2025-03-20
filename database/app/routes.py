from flask import render_template, flash, redirect
from app.forms import LoginForm
from app import app 

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Pieter'}
    posts = [
        {
            'author': {'username': 'Katie'},
            'body': 'This is awesome!'
        },
        {
            'author': {'username': 'Shane'},
            'body': 'This is written by me'
        }]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for the user {}, remember_me{}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign Up', form=form)