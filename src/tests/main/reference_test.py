import unittest
from ref.ref import Reference as ref
import db
from app import app
import random
import string

class TestReference(unittest.TestCase):

    def test_reference_goes_into_database(self):
        with app.app_context():
            random_keyword = get_random_string(8)
            self.assertEqual(ref.create_book_reference(1, random_keyword,"seppälä", "emilia", "kuinka koodata", 1234, "otava"), True)

    def test_cant_add_reference_with_same_keyword(self):
        with app.app_context():
            ref.create_book_reference(34, "abcdefg", "kalliokoski", "janika", "metsässä", 2001, "otava")
            self.assertEqual(ref.create_book_reference(1, "abcdefg","seppälä", "emilia", "kuinka koodata", 1234, "otava"), False)

    def test_empty_books_works(self):
        with app.app_context():
            ref.empty_books()
            length = len(ref.fetch_books())
            self.assertEqual(length, 0)
    
    def test_create_website(self):
        with app.app_context():
            random_keyword = get_random_string(8)
            self.assertEqual(ref.create_website_reference(5, random_keyword, "1234", "seppälä", "emilia", "nettisivu", "nettisivu", "nettisivu.net", "1234"), True)

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", result_str)