from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required
from .. import db
from ..models import User
from .forms import LoginForm
from . import main
from .. import dashboard


@main.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember.data)
        #import pdb; pdb.set_trace()
        return redirect('/view_books')
        flash('Invalid username or password.')
    return render_template('index.html', form=form)


@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.login'))