import unittest
import reference

class Testreference(unittest.TestCase):

    def test_books_amount_gets_bigger_when_book_added(self):
        books_amount = reference.books_amount()
        reference.create_book_reference(20, "abc", "emilia", "kuinka koodata", "otava")
        self.assertEqual(reference.books_amount(), books_amount + 1)
