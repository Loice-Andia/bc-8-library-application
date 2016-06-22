from flask import Flask
from flask_login import LoginManager, UserMixin
from . import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import PasswordType, force_auto_coercion
from datetime import datetime
import passlib


force_auto_coercion()


class User(UserMixin, db.Model):

    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(120), unique=True)
    name = db.Column(db.String(200), nullable=False)
    password = db.Column(PasswordType(onload=lambda **kwargs: dict(
        schemes=[
            'pbkdf2_sha512',
            'md5_crypt'
        ],
        deprecated=['md5_crypt'],
        **kwargs
    ), ), unique=False, nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)

    def verify_password(self, password):

        return self.password == password

    def __repr__(self):
        return '<Name %r>' % self.name


class Book(db.Model):

    __tablename__ = "book"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False, unique=True)
    authors = db.Column(db.String(200), nullable=False)
    quantity = db.Column(db.Integer, nullable=True)
    category = db.Column(db.String(200), nullable=True)


class Borrow_log(db.Model):

    __tablename__ = "borrow_log"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User',
                           backref=db.backref('borrow_log', lazy='dynamic'))
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    book = db.relationship('Book',
                           backref=db.backref('borrow_log', lazy='dynamic'))
    borrow_date = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)
