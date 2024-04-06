from app.extensions import db

class Book(db.Document):
    title = db.StringField(required=True)
    author = db.StringField(required=True)
    genre = db.StringField(required=True)
    isbn = db.StringField(required=True)
