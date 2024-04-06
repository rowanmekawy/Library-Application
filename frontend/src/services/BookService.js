import axios from 'axios';

const API_URL = 'http://localhost:5000/api/books';


class BookService {
  getAllBooks() {
    return axios.get(API_URL);
  }

  getBookById(bookId) {
    return axios.get(`${API_URL}/${bookId}`);
  }

  createBook(bookData) {
    return axios.post(API_URL, bookData);
  }

  updateBook(bookId, bookData) {
    return axios.put(`${API_URL}/${bookId}`, bookData);
  }

  deleteBook(bookId) {
    return axios.delete(`${API_URL}/${bookId}`);
  }
}

export default new BookService();
