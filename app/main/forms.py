from flask_wtf import Form
from wtforms import PasswordField
from wtforms.fields.html5 import EmailField
from wtforms import BooleanField, SubmitField, ValidationError, validators
from ..models import User


class LoginForm(Form):
    '''This class creates creates a
    Login form
    '''
    email = EmailField('Email address',
    	[validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', [validators.Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Log In', render_kw={"class": "form-group btn bg-blue btn-block btn-lg"})

