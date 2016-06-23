from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, login_required
from .. import db
from ..models import Book, Borrow_log, User
from . import admin
from .forms import AddBookForm


@admin.route('/add_book', methods=['GET', 'POST'])
@login_required
def add_book():
    '''Input function to add a new book.
    '''
    if request.method == "POST":
        form = {'title': request.form['title'],
                    'authors': request.form['authors'],
                    'category': request.form['category'],
                    'quantity': request.form['quantity']
                    }
        book = Book(**form)
        db.session.add(book)
        db.session.commit()
        flash('Book added ')
        return redirect(url_for('dashboard.view_books'))
    return render_template('admin/add_book.html')

@admin.route('/borrowed_books', methods=['GET', 'POST'])
@login_required
def view_borrowed_books():
    '''View function to show all borrowed books.
    '''
    borrowed_books = Borrow_log.query.all()
    return render_template('admin/borrowed_books.html', borrowed_books=borrowed_books)

@admin.route('/edit_book', methods=['GET', 'POST'])
@login_required
def edit_book():
    '''View function to edit a book.
    '''
    pass

@admin.route('/delete_book', methods=['GET', 'POST'])
@login_required
def delete_book():
    '''View function to delete a book.
    '''
    pass

@admin.route('/return_book', methods=['GET', 'POST'])
@login_required
def return_book():
    '''View function to return a book.
    '''
    pass