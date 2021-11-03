import pdb
from models.book import Book
from models.author import Author

from repositories import author_repository
from repositories import book_repository

author1 = Author("Jane Austen")
author_repository.save(author1)

authors_list = author_repository.select_all()
for author in authors_list:
    print(author.__dict__)

pdb.set_trace()
