from flask_restx import Resource, fields
from .models import Book
from ..api import api
from ..exceptions import InvalidInputError


book_model = api.model('Book', {
    'id': fields.String(required=True, description='The book ID'),
    'title': fields.String(required=True, description='The book title'),
    'author': fields.String(required=True, description='The author of the book'),
    'genre': fields.String(required=True, description='The genre of the book'),
    'isbn': fields.String(required=True, description='The ISBN of the book')
})

book_model_response = api.model('Book', {
    '_id': fields.String(required=True, description='The book ID'),
    'title': fields.String(required=True, description='The book title'),
    'author': fields.String(required=True, description='The author of the book'),
    'genre': fields.String(required=True, description='The genre of the book'),
    'isbn': fields.String(required=True, description='The ISBN of the book')
})

@api.route('/api/books')
class BookList(Resource):
    print("****************************************************")
    @api.marshal_list_with(book_model_response)
    def get(self):
        print("mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm")
        books_data = Book.objects.all()
        return [book.to_mongo().to_dict() for book in books_data]

    @api.expect(book_model)
    @api.marshal_with(book_model, code=201)
    def post(self):
        data = api.payload
        book = Book(**data).save()
        return book, 201

@api.route('/api/books/<book_id>')
@api.param('book_id', 'The book identifier')
@api.response(404, 'Book not found')
class BookApi(Resource):
    @api.marshal_with(book_model)
    def get(self, book_id):
        book = Book.objects(id=book_id).first()
        if book:
            return book
        raise InvalidInputError(f"Book with ID {book_id} not found")

    @api.expect(book_model)
    @api.marshal_with(book_model)
    def put(self, book_id):
        data = api.payload
        book = Book.objects(id=book_id).first()
        if book:
            book.update(**data)
            return book.reload()
        raise InvalidInputError(f"Book with ID {book_id} not found")

    @api.response(204, 'Book deleted')
    def delete(self, book_id):
        book = Book.objects(id=book_id).first()
        if book:
            book.delete()
            return '', 204
        raise InvalidInputError(f"Book with ID {book_id} not found")
