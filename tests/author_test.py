import unittest
from models.author import Author

class TestAuthor(unittest.TestCase):

    def setUp(self):
        self.author1 = Author("Jane Austen")

    def test_author_has_name(self):
        self.assertEqual("Jane Austen", self.author1.name)

    def test_author_has_id(self):
        self.assertEqual(None, self.author1.id)