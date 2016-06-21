from flask import Flask, render_template, request
from flask_login import login_required
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import PasswordType, force_auto_coercion
import passlib


force_auto_coercion()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://lolo:lolo@localhost:5432/library_application'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


# Create our database model
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(120), unique=True)
    name = db.Column(db.String(200), nullable=False)
    password = db.Column(PasswordType(
        schemes=[
            'pbkdf2_sha512',
            'md5_crypt'
        ],
        deprecated=['md5_crypt']
    ), unique=False, nullable=False)
    role = db.Column(db.String(50), nullable=False)

    def __init__(self, email, password, name, role):
        self.email = email
        self.password = password
        self.name = name
        self.role = role

    def __repr__(self):
        return '<E-mail %r>' % self.email


# Set "homepage" to index.html
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/memberdashboard')
@login_required
def memberdashboard():
    return render_template("dashboard.html")

# Save user details to database and send to dashboard page
@app.route('/authenticate', methods=['POST'])
def authenticate():
    email = None
    name = None
    password = None
    role = None
    if request.method == 'POST':
        email = request.form['email']
        # Check that email does not already exist (not a great query, but works)
        if not db.session.query(User).filter(User.email == email).count():
            reg = User(email, name, password, role)
            db.session.add(reg)
            db.session.commit()
            return render_template('index.html')
    return render_template('signup.html')


# authenticate user
@app.route('/login', methods=['POST'])
def login():
    email = None
    if request.method == 'POST':
        email = request.form['email']
        # Check that email does not already exist (not a great query, but works)
        if not db.session.query(User).filter(User.email == email).count():
            reg = User(email)
            db.session.add(reg)
            db.session.commit()
            return render_template('dashboard.html')
    return render_template('index.html')
if __name__ == '__main__':
    app.debug = True
    app.run()
