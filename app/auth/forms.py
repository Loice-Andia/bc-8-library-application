from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField
from wtforms import SubmitField, ValidationError, validators
from wtforms.fields.html5 import EmailField
from ..models import User
from ..main import forms


class RegistrationForm(forms.LoginForm):
    '''This class extends the Login form and
    creates a user registration form.
    '''
    name = StringField('Name', [validators.Required()])
    email = EmailField(
        'Email Address',
        [
            validators.Required(),
            validators.Length(
                min=6, max=64, message='Your email is invalid')
        ]
    )
    password = PasswordField('Password', [validators.Required(),
                                          validators.EqualTo(
        'password_confirmation',
        'Passwords do not match.'
    )])
    password_confirmation = PasswordField('Password Confirmation',
                                          [validators.Required()])
    is_admin = BooleanField('Are you an Admin')
    submit = SubmitField('Submit', render_kw={"class": "btn bg-blue btn-block btn-lg"})
    remember = None

    def validate_username(self, field):
        '''This method checks if a username already exists in
        the database
        '''
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')
