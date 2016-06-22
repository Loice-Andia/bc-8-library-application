from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, login_required
from .. import db
from ..models import Book, Borrow_log
from . import admin
from .forms import AddBookForm


@admin.route('/add_book', methods=['GET', 'POST'])
@login_required
def add_book():
    '''Input function to add a new book.
    '''
    form = AddBookForm()
    if request.method == "POST" and form.validate_on_submit():
        book = Book(title=form.title.data,
                    authors=form.authors.data,
                    category=form.category.data,
                    quantity=form.quantity.data,)
        db.session.add(book)
        db.session.commit()
        flash('Book added ')
        return redirect(url_for('dashboard.view_books'))
    return render_template('admin/add_book.html', form=form)

@admin.route('/borrowed_books', methods=['GET', 'POST'])
@login_required
def view_borrowed_books():
    '''View function to show all borrowed books.
    '''
    pass

@admin.route('/edit_book', methods=['GET', 'POST'])
@login_required
def edit_book():
    '''View function to edit a book.
    '''
    pass

@admin.route('/delete_book', methods=['GET', 'POST'])
@login_required
def delete_book():
    '''View function to edit a book.
    '''
    pass