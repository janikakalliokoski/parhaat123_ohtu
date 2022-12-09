import unittest
from services.reference_service import ReferenceService
import db
from app import app
import random
import string

class FakeReferenceRepo:
    def __init__(self):
        self.references = []
        self.books = []

    def create_new_reference(self, ref_id, reference):
        self.references.append((ref_id, reference))

    def create_new_book_reference(self, reference_id, keyword,
                            author_surname, author_name, title, year, publisher):
        self.books.append((reference_id, keyword,
                            author_surname, author_name, title, year, publisher))

    def fetch_books(self):
        return self.books

    def get_all_references(self):
        return self.references

    def empty_books(self):
        self.books = []

class TestReferenceService(unittest.TestCase):
    def setUp(self):
        self.reference_service = ReferenceService(FakeReferenceRepo())

    def test_reference_goes_into_database(self):
        self.reference_service.create_new_book_reference(38, "reference_service", "kalliokoski", "janika", "metsässä", 2001, "otava")
        self.assertEqual(len(self.reference_service.get_all_books()), 1)

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", result_str)
