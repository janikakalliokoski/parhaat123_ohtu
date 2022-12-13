import unittest
import random
import string
from services.reference_service import ReferenceService
import db
from app import app

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

    def remove_all_books(self):
        self.books = []

class TestReferenceService(unittest.TestCase):
    def setUp(self):
        self.reference_service = ReferenceService(FakeReferenceRepo())

    def test_add_book_reference_successfully(self):
        self.reference_service.create_new_book_reference(
            38, "reference_service", "kalliokoski", "janika", "metsässä", 2001, "otava")
        self.assertEqual(len(self.reference_service.get_all_books()), 1)

    def test_cannot_add_book_without_keyword(self):
        self.reference_service.create_new_book_reference(
            3, "", "kalliokoski", "janika", "metsässä", 2001, "otava")
        self.assertEqual(len(self.reference_service.get_all_books()), 0)

    def test_year_cannot_contain_letters(self):
        self.reference_service.create_new_book_reference(
            45, "abc123", "janika", "kallio", "entiedä", "20s", "otava"
        )
        self.assertEqual(len(self.reference_service.get_all_books()), 0)

    def test_remove_all_books(self):
        self.reference_service.create_new_book_reference(
            8, "123", "kalliokoski", "janika", "metsässä", 2001, "otava")
        self.reference_service.create_new_book_reference(
            9, "abc", "kalliokoski", "janika", "metsässä", 2001, "otava")
        self.reference_service.remove_all_books()
        self.assertEqual(len(self.reference_service.get_all_books()),0)

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", result_str)
