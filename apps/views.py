from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@localhost:3306/books"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
all_book=[]

from apps.models import Book

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        rating = request.form["rating"]
        new_book = Book(title=title, author=author, rating=rating)
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('add.html')

@app.route('/')
def home():
    ##READ ALL RECORDS
    all_books = db.session.query(Book).all()
    return render_template("index.html", books=all_books)

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)



