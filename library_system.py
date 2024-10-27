import os

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"{self.title} by {self.author} - ISBN: {self.isbn}"

class Library:
    def __init__(self, file_path="library.txt"):
        self.file_path = file_path
        self.books = []
        self.load_books()

    def load_books(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                for line in file:
                    title, author, isbn = line.strip().split(";")
                    self.books.append(Book(title, author, isbn))

    def save_books(self):
        with open(self.file_path, "w") as file:
            for book in self.books:
                file.write(f"{book.title};{book.author};{book.isbn}\n")

    def add_book(self, book):
        self.books.append(book)
        self.save_books()
        print(f"Book '{book.title}' added.")

    def remove_book(self, isbn):
        self.books = [book for book in self.books if book.isbn != isbn]
        self.save_books()
        print(f"Book with ISBN '{isbn}' removed.")

    def search_books(self, title=None, author=None):
        results = [book for book in self.books if (title and title in book.title) or (author and author in book.author)]
        for book in results:
            print(book)

library = Library()
library.add_book(Book("madol duuwa", "martin wickramasinghe", "123456789"))
library.add_book(Book("plane trigonometry", "s.l.loney", "1023456789"))
library.search_books(title="plane trigonometry")
library.remove_book("123456789")
