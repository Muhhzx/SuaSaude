from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from extensions import db
from models.user import User 

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods =['GET', 'POST'])
def login(): 
    if current_user.is_authenticated:
        return redirect(url_for('auth.dashboard'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('auth.dashboard'))
        else:
            flash('Usuário ou senha inválidos')
            return render_template('login.html')
        
@auth_bp.route('logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('auth.dashboard'))
    if request.method == 'POST':
       username = request.form['username']
       password = request.form['password']
       if User.query.filter_by(username=username).first():
            flash('Usuário já existe')
       else:
           user = User (username=username)
           user.set_password(password)
           db.session.add(user)
           db.session.commit()
           flash('Usuário criado com sucesso, muito obrigado por se registrar')
           return redirect(url_for('auth.login'))