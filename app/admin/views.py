from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, login_required
from .. import db
from ..models import Book, Borrow_log, User
from . import admin
from .forms import AddBookForm
import datetime

now = datetime.datetime.utcnow()

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

@admin.route('/edit_book/<book_id>', methods=['GET', 'POST'])
@login_required
def edit_book(book_id):
    '''View function to edit a book.
    '''
    pass

@admin.route('/delete_book/<book_id>', methods=['GET', 'POST'])
@login_required
def delete_book(book_id):
    '''View function to delete a book.
    '''
    book = Book.query.filter_by(id=book_id).first()
    try:
        db.session.delete(book)
        db.session.commit()
        flash('book deleted')
        return redirect(url_for('dashboard.view_books'))
    except:
        flash('Book record not deleted')
        return redirect(url_for('dashboard.view_books'))

@admin.route('/return_book/<borrow_log_id>', methods=['GET', 'POST'])
@login_required
def return_book(borrow_log_id):
    '''View function to return a book.
    '''
    borrowed_book = Borrow_log.query.filter_by(id=borrow_log_id).first()
    book = Book.query.filter_by(id=borrowed_book.book_id).first()
    borrow_period = now.day - borrowed_book.borrow_date.day
    if borrow_period <= 5:
        fee = 0
    else:
        fee = borrow_period*15
    #print fee
    try:
        db.session.delete(borrowed_book)
        book.quantity +=1
        db.session.add(book)
        db.session.commit()
        flash('To Pay :', fee)
        return redirect(url_for('admin.view_borrowed_books'))
    except:
        flash('Book return failed')
        return redirect(url_for('admin.view_borrowed_books'))
