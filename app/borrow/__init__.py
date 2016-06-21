from flask import Blueprint

borrow = Blueprint('borrow', __name__)

from . import views