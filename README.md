# Library Application

## Introduction
*  **Library Application`** is a Flask Application.
*  It has the following features;
  * A user should be able to signup.
  * A user should be able to login.
  * A user should be able to view all the books in the library.
  * A user should be able to borrow an available book.
  * An admin should be able to mark a book as returned. 
  * An admin should be able to manage all the books in the library 
  	* Create new books, add quantities and categorise books
  	* Delete books from the library
  	* Surcharging for lately returned books

*  Click [here](http://bc-8-maktaba.herokuapp.com/) to access the app on Heroku

## Installation and setup
*  Navigate to a directory of choice on `terminal`.
*  Clone this repository on that directory.
  *  Using SSH;

    >`git@github.com:Loice-Andia/bc-8-library-application.git`

  *  Using HTTPS;

    >`https://github.com/Loice-Andia/bc-8-library-application.git`

*  Navigate to the repo's folder on your computer
  *  `cd bc-8-library-application/`
*  Install the app's backend dependencies. For best results, using a [virtual environment](http://virtualenv.readthedocs.org/en/latest/installation.html) is recommended.
  *  `pip install -r requirements`
*  Install the app's database and set it up. The default `PostgreSQL` was used for development.
*  Create and apply migrations
  *  `python manage.py db init`
  *  `python manage.py db migrate`
  *  `python manage.py db upgrade`
* Run the app
  *  `python manage.py runserver`
* Open the app on your browser: (http://127.0.0.1:5000/)