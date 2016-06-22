from flask_wtf import Form
from wtforms import StringField, IntegerField, TextAreaField
from wtforms import SubmitField, ValidationError, validators
from ..models import Book


class AddBookForm():
    '''This class creates a form for the admin to add new books.
    '''
    title = StringField('Title', [validators.Required()])
    authors = StringField('Authors', [validators.Required()])
    category = TextAreaField('Category', [validators.Required()])
    quantity = IntegerField('Quantity', [validators.Required()])
    submit = SubmitField('Submit')

    def validate_title(self, field):
        #This method checks if same book title already exists in
        #the database
        
        if Book.query.filter_by(title=field.data).first():
            raise ValidationError('Book already exists.')
