import json

class Book:
    def __init__(self, title, author, isbn):
        """
        Initialize a Book object with title, author, and ISBN.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The ISBN of the book.
        """
        self.title = title
        self.author = author
        self.isbn = isbn

class Library:
    def __init__(self, storage_file="books.json"):
        """
        Initialize a Library object with a storage file for books.

        Args:
            storage_file (str, optional): The file path for storing book data. Defaults to "books.json".
        """
        self.storage_file = storage_file
        self.books = []

    def add_book(self, title, author, isbn):
        """
        Add a new book to the library.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The ISBN of the book.
        """
        self.books.append(Book(title, author, isbn))
        self._save_books()

    def list_books(self):
        """List all the books in the library."""
        for idx, book in enumerate(self.books, 1):
            print(f"{idx}. Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}")

    def _save_books(self):
        """Save the list of books to the storage file."""
        try:
            with open(self.storage_file, 'w') as file:
                json.dump([vars(book) for book in self.books], file)
        except Exception as e:
            print(f"Error saving books: {e}")

    def load_books(self):
        """Load the list of books from the storage file."""
        try:
            with open(self.storage_file, 'r') as file:
                data = file.read()
                if data:  # Check if data is not empty
                    self.books = [Book(**book_data) for book_data in json.loads(data)]
                else:
                    print("The file is empty.")
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading books: {e}")
            self.books = []

# Usage example:
# library = Library()
# library.load_books()
# library.add_book("Title", "Author", "1234567890")
# library.list_books()
