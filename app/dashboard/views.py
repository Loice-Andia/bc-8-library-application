from flask import render_template, flash
from flask_login import login_required
from . import dashboard
from .. import db
from ..models import Book, Borrow_log
#from .forms import view_books


@dashboard.route('/view_books', methods=['GET', 'POST'])
@login_required
def view_books():
    '''View function to return all books.
    '''
    book = Book.query.all()
    return render_template('dashboard/view_books.html', book=book)


@dashboard.route('/my_books', methods=['GET', 'POST'])
@login_required
def my_books():
    '''View function to books borrowed by a specific user.
    '''
    borrowed_books = Borrow_log.query.all()
    return render_template('dashboard/my_books.html', borrowed_books=borrowed_books)