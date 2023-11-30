from flask import Flask
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
    
with app.app_context():
    # Creating a record
    db.create_all()   
    # book = Books(
    #     title = "New132",
    #     author = "estset123es",
    #     rating = 1.6
    # )
    # db.session.add(book)
    # db.session.commit()
    
    # Reading records
    result = db.session.execute(db.select(Books).order_by(Books.title))
    all_books = result.scalars()
    for book in all_books:
        print(book.title)
        
    # Get a specific Record
    book = db.session.execute(db.select(Books).where(Books.title == "Harry Potter and the Chamber of Secrets")).scalar()
    
    # Update an entry
    book_to_update = db.session.execute(db.select(Books).where(Books.title == "Harry Potter and the Goblet of Fire")).scalar()
    book_to_update.title = "Harry Potter and the Goblet of Fire"
    book_to_update.author = "J. K. Rowling"
    db.session.commit() 
    
    # Update an entry by primary key
    book_id = 1
    book_to_update = db.session.execute(db.select(Books).where(Books.id == book_id)).scalar()
    # or book_to_update = db.get_or_404(Book, book_id)  
    book_to_update.title = "Harry Potter and the Goblet of Fire"
    db.session.commit()
    
    # Delete Entry
    book_to_delete = db.session.execute(db.select(Books).where(Books.id == book_id)).scalar()
    # or book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()