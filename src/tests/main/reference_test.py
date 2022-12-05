import unittest
from ref.ref import Reference as ref
import db
from app import app

class TestReference(unittest.TestCase):

    def test_books_amount_gets_bigger_when_book_added(self):
        with app.app_context():
            books_amount = ref.books_amount()
            ref.create_book_reference(20, "abc", "emilia", "kuinka koodata", "otava")
            self.assertEqual(ref.books_amount(), books_amount + 1)
