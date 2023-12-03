from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-movie-collection.db"
db = SQLAlchemy()
db.init_app(app)

class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String, nullable=False)
    img_url = db.Column(db.String, nullable=False)
    
class EditForm(FlaskForm):
    rating = StringField(label='Rating', validators=[DataRequired()])
    review = StringField(label='Your Review', validators=[DataRequired()])
    submit = SubmitField(label="Save")


@app.route("/")
def home():
    with app.app_context():
        db.create_all()
        result = db.session.execute(db.select(Movies).order_by(Movies.ranking))
        all_movies = result.scalars()
        return render_template("index.html", movies=all_movies)
    
@app.route("/update/<id>", methods=["GET", "POST"])
def update(id):
    edit_form = EditForm()
    if edit_form.validate_on_submit():
        print(edit_form.rating.data)
        movie_to_update = db.session.execute(db.select(Movies).where(Movies.id == id)).scalar()
        movie_to_update.rating = float(edit_form.rating.data)
        movie_to_update.review = edit_form.review.data
        db.session.commit()
        return redirect("/")
    return render_template("edit.html", id=id, form=edit_form)

@app.route("/delete/<id>", methods=["GET"])
def delete(id):
    with app.app_context():
        db.create_all()
        movie_to_delete = db.session.execute(db.select(Movies).where(Movies.id == id)).scalar()
        db.session.delete(movie_to_delete)
        db.session.commit()
        return redirect("/")
@app.route("/add")
def add():
    return render_template("add.html")

if __name__ == '__main__':
    app.run(debug=True)
