import unittest
from ref.ref import Reference as ref
import db
from app import app
import string
import random

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", result_str)

class TestReference(unittest.TestCase):

    def test_books_amount_gets_bigger_when_book_added(self):
        with app.app_context():
            self.assertEqual(ref.create_book_reference(1, "abc","seppälä", "emilia", "kuinka koodata", 1234, "otava"), True)