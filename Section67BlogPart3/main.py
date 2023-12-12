from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date

app = Flask(__name__)
ckeditor = CKEditor(app)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy()
db.init_app(app)



# CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


with app.app_context():
    db.create_all()
    
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


@app.route('/')
def get_all_posts():
    result = db.session.execute(db.select(BlogPost).order_by(BlogPost.date))
    all_posts = result.scalars().all()
    posts = []
    for post in all_posts:
        post_obj = {
            "id": post.id,
            "title": post.title,
            "subtitle": post.subtitle,
            "date": post.date,
            "body": post.body,
            "author": post.author,
            "img_url": post.img_url
        }
        posts.append(post_obj)
    return render_template("index.html", all_posts=posts)

@app.route('/post')
def show_post():
    query_location = request.args.get("post_id")
    result = db.session.execute(db.select(BlogPost).where(BlogPost.id == query_location))
    requested_post = result.scalar()
    return render_template("post.html", post=requested_post)


@app.route("/new-post", methods=["POST", "GET"])
def create_post():
    if request.method == "GET":
        form = CreatePostForm()
        return render_template("make-post.html", form=form)
    else:
        today = date.today()
        formatted_date = today.strftime("%B %d, %Y")
        new_post = BlogPost(
            title = request.form.get("title"),
            subtitle = request.form.get("subtitle"),
            date = formatted_date,
            body = request.form.get("body"),
            author = request.form.get("author"),
            img_url = request.form.get("img_url")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
        
        

@app.route("/edit-post/<post_id>", methods=["POST", "GET"])
def edit_post(post_id):
    if request.method == "GET":
        result = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id))
        requested_post = result.scalar()
        form = CreatePostForm(title=requested_post.title,
            subtitle=requested_post.subtitle,
            img_url=requested_post.img_url,
            author=requested_post.author,
            body=requested_post.body
        )
        return render_template("make-post.html", post=requested_post, form=form)
    else:
        post = db.get_or_404(BlogPost, post_id)
        today = date.today()
        formatted_date = today.strftime("%B %d, %Y")
        post.title = request.form.get("title")
        post.subtitle = request.form.get("subtitle")
        post.date = formatted_date
        post.body = request.form.get("body")
        post.author = request.form.get("author")
        post.img_url = request.form.get("img_url")
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    
    
    

# TODO: delete_post() to remove a blog post from the database

@app.route("/delete/<post_id>")
def delete_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
