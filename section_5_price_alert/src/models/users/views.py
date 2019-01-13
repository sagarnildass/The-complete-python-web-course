from flask import Blueprint, session, request, url_for, render_template
from models.users.user import User
from werkzeug.utils import redirect
import models.users.errors as UserErrors

user_blueprint = Blueprint('users', __name__)

@user_blueprint.route('/login', methods=['GET', 'POST'])
def login_user():
    if request.method == 'POST':
        #check the login is valid
        email = request.form['email']
        password = request.form['hashed']
        try:
            if User.is_login_valid(email, password):
                session['email'] = email
                return redirect(url_for('users.user_alerts'))
        except UserErrors.UserError as e:
            return e.message

    return render_template('users/login.jinja2')

@user_blueprint.route('/register', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        #check the login is valid
        email = request.form['email']
        password = request.form['hashed']
        try:
            if User.register_user(email, password):
                session['email'] = email
                return redirect(url_for('users.user_alerts'))
        except UserErrors.UserError as e:
            return e.message

    return render_template('users/register.jinja2')


@user_blueprint.route('/alerts')
def user_alerts():
    return "This is the alerts page"

@user_blueprint.route('/logout')
def logout_user():
    pass

@user_blueprint.route('/check_alerts/<string:user_id>')
def check_user_alerts(user_id):
    pass
