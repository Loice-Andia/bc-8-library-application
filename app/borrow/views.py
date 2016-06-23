from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, login_required
from .. import db
from ..models import Book, Borrow_log, User
from . import borrow


@borrow.route('/borrow_book/<book_id>/<name>', methods=['GET', 'POST'])
@login_required
def borrow_book(book_id, name):
    '''View function that allows a user to borrow a book
     and redirects to the my books page.
    '''
    user = User.query.filter_by(name=name).first()
    try:
    	print(book_id,name)

        form = {'user_id': user.id,
                'book_id': book_id
                }
  
        borrow_log = Borrow_log(**form)
        db.session.add(borrow_log)
        db.session.commit()
        flash('Book borrowed')
        return redirect(url_for('dashboard.my_books'))
    except:
		flash('Book borrowing failed')
		return redirect(url_for('dashboard.view_books'))
