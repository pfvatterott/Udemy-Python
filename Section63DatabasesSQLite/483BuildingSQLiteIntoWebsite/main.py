from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db = SQLAlchemy()
db.init_app(app)

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    author = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)


@app.route('/')
def home():
    with app.app_context():
        db.create_all()
        result = db.session.execute(db.select(Books).order_by(Books.title))
        all_books = result.scalars()
        return render_template('index.html', books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template('add.html')
    else:
        with app.app_context():
            db.create_all()
            book = Books(
                title = request.form["title"],
                author = request.form["author"],
                rating = float(request.form["rating"])
            )
            db.session.add(book)
            db.session.commit()
        return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True)

