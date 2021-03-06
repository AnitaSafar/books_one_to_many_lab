import pdb
from models.book import Book
from models.author import Author

from repositories import author_repository
from repositories import book_repository

author_repository.delete_all()
book_repository.delete_all()

author1 = Author("Jane Austen")
author_repository.save(author1)

authors_list = author_repository.select_all()
for author in authors_list:
    print(author.__dict__)

book1 = Book("Emma", author1)
book_repository.save(book1)
book2 = Book("Pride and Prejudice", author1)
book_repository.save(book2)

books_list = book_repository.select_all()
for book in books_list:
    print(book.__dict__)


pdb.set_trace()
