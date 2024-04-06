<template>
  <v-container fluid>
    <v-row>
      <v-col cols="12">
        <v-card flat>
          <v-card-title>
            <v-row no-gutters align="center" justify="space-between">
              <span class="headline">Books</span>
              <v-btn color="success" dark @click="createDialog = true">Add New Book</v-btn>
            </v-row>
          </v-card-title>
          <v-tabs fixed-tabs>
            <v-tab>All Books</v-tab>
            <v-tab>Most Popular</v-tab>
          </v-tabs>
          <v-card-text>
            <v-data-table
              :headers="headers"
              :items="books"
              item-key="id"
              class="elevation-0"
            >
              <template v-slot:[`item.actions`]="{ item }">
                <v-icon small class="mr-2" @click="openEditDialog(item)">
                  mdi-pencil
                </v-icon>
                <v-icon small @click="deleteBook(item._id)">
                  mdi-delete
                </v-icon>
              </template>
            </v-data-table>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
    <v-dialog v-model="createDialog" max-width="500px">
      <v-card>
        <v-card-title>Add New Book</v-card-title>
        <v-card-text>
          <v-form @submit.prevent="addNewBook">
            <v-text-field v-model="newBook.title" label="Title"></v-text-field>
            <v-text-field v-model="newBook.author" label="Author"></v-text-field>
            <v-text-field v-model="newBook.genre" label="Genre"></v-text-field>
            <v-text-field v-model="newBook.isbn" label="ISBN"></v-text-field>
          </v-form>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="createDialog = false">Cancel</v-btn>
          <v-btn color="blue darken-1" text @click="addNewBook">Create</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="editDialog" max-width="500px">
      <v-card>
        <v-card-title>Edit Book</v-card-title>
        <v-card-text>
          <v-form @submit.prevent="updateBook">
            <v-text-field v-model="editedBook.title" label="Title"></v-text-field>
            <v-text-field v-model="editedBook.author" label="Author"></v-text-field>
            <v-text-field v-model="editedBook.genre" label="Genre"></v-text-field>
            <v-text-field v-model="editedBook.isbn" label="ISBN"></v-text-field>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="editDialog = false">Cancel</v-btn>
              <v-btn color="blue darken-1" text @click="updateBook">Update</v-btn>
            </v-card-actions>
          </v-form>
        </v-card-text>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<style scoped>
.headline {
  font-size: 24px;
  font-weight: bold;
}

.v-card-title {
  padding-bottom: 0;
}

.v-btn {
  margin-left: 12px;
}

.v-tabs {
  border: none;
}

.v-tab {
  text-transform: none;
  font-weight: normal;
}

.v-icon {
  cursor: pointer;
}
</style>


<script>
import BookService from '@/services/BookService';

export default {
  name: 'BookList',
  data() {
    return {
      books: [],
      headers: [
        { title: 'title', value: 'title' },
        { title: 'Author', value: 'author' },
        { title: 'Genre', value: 'genre' },
        { title: 'ISBN', value: 'isbn' },
        { title: 'Actions', value: 'actions', sortable: false },
      ],
      createDialog: false,
      editDialog: false,
      newBook: {
        title: '',
        author: '',
        genre: '',
        isbn: '',
      },
      editedBook: {
        title: '',
        author: '',
        genre: '',
        isbn: '',
      },
    };
  },
  created() {
    this.fetchBooks();
  },
  methods: {
    fetchBooks() {
      BookService.getAllBooks()
        .then(response => {
          this.books = response.data;
        })
        .catch(error => {
          console.error('There was an error fetching the books:', error);
        });
    },
    addNewBook() {
      BookService.createBook(this.newBook)
        .then(() => {
          this.fetchBooks();
          this.createDialog = false;
          this.newBook = { title: '', author: '', genre: '', isbn: '' };
        })
        .catch(error => {
          console.error('There was an error adding the book:', error);
        });
    },
    openEditDialog(book) {
      this.editedBook = { ...book };
      this.editDialog = true;
    },
    updateBook() {
      const updatedBook = {
        title: this.editedBook.title,
        author: this.editedBook.author,
        genre: this.editedBook.genre,
        isbn: this.editedBook.isbn
      };
      BookService.updateBook(this.editedBook._id, updatedBook)
        .then(() => {
          this.fetchBooks();
          this.editDialog = false;
          this.editedBook = { title: '', author: '', genre: '', isbn: '' };
        })
        .catch(error => {
          console.error('There was an error updating the book:', error);
        });
    },
    deleteBook(bookId) {
      if (confirm('Are you sure you want to delete this book?')) {
        BookService.deleteBook(bookId)
          .then(() => {
            this.fetchBooks();
          })
          .catch(error => {
            console.error('There was an error deleting the book:', error);
          });
      }
    },
  },
};
</script>

