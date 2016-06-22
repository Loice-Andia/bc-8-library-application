from flask import render_template, redirect, request, url_for, flash
from . import auth
from .. import db
from ..models import User
from .forms import RegistrationForm


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        # get the user role default
        user = User(name=form.name.data,
                    email=form.email.data,
                    password=form.password.data,
                    is_admin=form.is_admin.data,)
        db.session.add(user)
        db.session.commit()
        flash('Welcome to Library Management! \n Please login to continue.')
        return redirect(url_for('main.login'))
    return render_template('signup.html', form=form)
