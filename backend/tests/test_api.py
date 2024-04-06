import pymongo
import pytest
from app.books.models import Book

@classmethod
def setUpClass(cls):
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client.test_database

    db.drop_collection('test_database')

    db.collection_name.insert_many([
        { 'name': 'test_document_1' },
        { 'name': 'test_document_2' }
    ])

    client.close()



def test_get_books(client):
    Book(title="Test Book", author="Test Author", genre="Test Genre", isbn="1234567890").save()
    response = client.get('/api/books')
    assert response.status_code == 200
    assert b"Test Book" in response.data

@pytest.mark.usefixtures('mongo')
def test_add_book(client):
    response = client.post('/api/books', json={
        'title': 'New Book',
        'author': 'New Author',
        'genre': 'New Genre',
        'isbn': '0987654321'
    })
    assert response.status_code == 201
    assert b"New Book" in response.data

def test_get_book(client):
    book = Book(title="Specific Book", author="Specific Author", genre="Specific Genre", isbn="1122334455").save()
    response = client.get(f'/api/books/{book.id}')
    assert response.status_code == 200
    assert b"Specific Book" in response.data

@pytest.mark.usefixtures('mongo')
def test_update_book(client):
    book = Book(title="Old Book", author="Old Author", genre="Old Genre", isbn="5566778899").save()
    response = client.put(f'/api/books/{book.id}', json={
        'title': 'Updated Book',
        'author': 'Updated Author',
        'genre': 'Updated Genre',
        'isbn': '9988776655'
    })
    assert response.status_code == 200
    assert b"Updated Book" in response.data

@pytest.mark.usefixtures('mongo')
def test_delete_book(client):
    book = Book(title="Delete Book", author="Delete Author", genre="Delete Genre", isbn="2233445566").save()
    response = client.delete(f'/api/books/{book.id}')
    assert response.status_code == 204
    assert Book.objects(id=book.id).first() is None
