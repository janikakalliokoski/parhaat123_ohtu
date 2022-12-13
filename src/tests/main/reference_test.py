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
        self.websites = []

    def create_new_book_reference(self, reference_id, keyword,
                            author_surname, author_name, title, year, publisher):
        self.books.append((reference_id, keyword,
                            author_surname, author_name, title, year, publisher))
        self.references.append("kirja")

    def fetch_books(self):
        return self.books

    def get_all_references(self):
        return self.references

    def remove_all_books(self):
        self.books = []

    def fetch_websites(self):
        return self.websites

    def remove_all_websites(self):
        self.websites = []

    def create_website_reference(self, reference_id, keyword,
        added_at, author_surname, author_name, title, description, url, year):
        self.websites.append((reference_id, keyword,
        added_at, author_surname, author_name, title, description, url, year))
        self.references.append("verkkosivu")

    def get_book_by_keyword(self, keyword):
        for book in self.books:
            if book[0] == keyword:
                return book

    def get_website_by_keyword(self, keyword):
        for website in self.websites:
            if website[0] == keyword:
                return website

    def remove_reference(self, keyword):
        for ref in self.references:
            if ref[0] == keyword:
                self.references.remove(ref)

    def remove_book_reference(self, keyword):
        for ref in self.books:
            if ref[0] == keyword:
                self.books.remove(ref)

    def remove_website_reference(self, keyword):
        for ref in self.websites:
            if ref[0] == keyword:
                self.websites.remove(ref)

    def get_book_references_normal(self):
        return self.books

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

    def test_remove_book_reference_by_id(self):
        self.reference_service.create_new_book_reference(
            54, "5454", "home", "juusto", "lautasella", 2022, "otava")
        self.reference_service.create_new_book_reference(
            55, "5555", "leipä", "juusto", "lautasella", 2022, "otava")
        self.reference_service.remove_reference(54)
        self.assertEqual(len(self.reference_service.get_all_books()), 1)

    def test_remove_website_reference_by_id(self):
        self.reference_service.create_website_reference(
            9999, "8888", "12122020", "kerma", "juusto",
            "lautasella","tällane", "www.juustot.fi", "2022")
        self.reference_service.create_website_reference(
            9998, "8887", "12122020", "brie", "juusto",
            "lautasella","tällane", "www.juustot.fi", "2022")
        self.reference_service.remove_reference(9999)
        self.assertEqual(len(self.reference_service.get_all_websites()), 1)

    def test_gets_all_references(self):
        self.reference_service.create_new_book_reference(
            50, "5450", "sulate", "juusto", "lautasella", 2022, "otava")
        self.assertEqual(len(self.reference_service.get_all_references()), 1)

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", result_str)
