import unittest
from models.book import Book
from models.author import Author

class TestBook(unittest.TestCase):

    def setUp(self):
        self.author1 = Author("Jane Austen")
        self.book1 = Book("Emma", self.author1)

    def test_book_has_title(self):
        self.assertEqual("Emma", self.book1.title)

    def test_book_has_author(self):
        self.assertEqual(self.author1, self.book1.author)

    def test_book_has_id(self):
        self.assertEqual(None, self.book1.id)
