from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, login_required
from .. import db
from ..models import Book, Borrow_log, User
from . import borrow
#from .forms import AddBookForm


@borrow.route('/borrow_book', methods=['GET', 'POST'])
@login_required
def borrow_book():
    '''View function that allows a user to borrow a book.
    '''
    pass