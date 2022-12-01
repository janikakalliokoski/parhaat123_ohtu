import unittest
import ref.ref as ref

class Testreference(unittest.TestCase):

    def test_books_amount_gets_bigger_when_book_added(self):
        books_amount = ref.books_amount()
        ref.create_book_reference(20, "abc", "emilia", "kuinka koodata", "otava")
        self.assertEqual(ref.books_amount(), books_amount + 1)
