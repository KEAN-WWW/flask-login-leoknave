from application.bp.authentication.forms import LoginForm
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from application.database import User

authentication = Blueprint('authentication', __name__, template_folder='templates')

@authentication.route('/registration', methods=['GET', 'POST'])
def registration():
    pass  # Leave registration empty for now

@authentication.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User.query.filter_by(email=email).first()

        if not user:
            flash('User Not Found', 'danger')
            return redirect(url_for('authentication.login'))

        if not user.check_password(password):
            flash('Password Incorrect', 'danger')
            return redirect(url_for('authentication.login'))

        login_user(user)
        return redirect(url_for('authentication.dashboard'))

    return render_template('login.html', form=form)

@authentication.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', user=current_user)

@authentication.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('homepage.homepage'))



