from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.users_model import User
from flask_app import bcrypt

@app.route('/')
def index():
    return redirect('/user/login')

@app.route('/user/login')
def login():
    if 'user_id' in session:
        return redirect('/dashboard')
    return render_template('index.html', users = User.get_users())

@app.route('/user/login/success', methods = ['POST'])
def login_success():
    user = User.validate_login(request.form)
    if not user:
        return redirect('/dashboard')

@app.route('/user/register', methods = ['POST'])
def register_success():
    if not User.validate_register(request.form):
        return redirect('/dashboard')
    User.create_user(request.form)
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect ('/user/logout')

@app.route('/user/logout')
def exit():
    if 'user_id' in session:
        session.clear()
    return redirect('/')