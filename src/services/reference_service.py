import repositories.ref_repo as refe

class ReferenceService:
    def __init__(self, viiterepo=refe.viiterepositorio):
        self.viitteet = viiterepo

    def get_all_books(self):
        return self.viitteet.fetch_books()

    def remove_all_books(self):
        self.viitteet.remove_all_books()

    def create_reference(self, ref_type):
        return self.viitteet.create_reference(ref_type)

    def get_references(self):
        books = self.viitteet.get_book_references_normal()
        websites = self.viitteet.get_website_references_normal()
        books_normal = []
        books_bibtex = []
        websites_normal = []
        websites_bibtex = []
        if books:
            for book in books:
                # tänne tulee books[0] et saadaan keyword poistoo varten helposti
                books_normal.append((self.format_books_normal(book), book[0]))
                books_bibtex.append(self.format_books_bibtex(book))
        if websites:
            for website in websites:
                websites_normal.append((self.format_websites_normal(website), website[0]))
                websites_bibtex.append(self.format_websites_bibtex(website))
        refs_bibtex = books_bibtex + websites_bibtex
        refs_normal = books_normal + websites_normal
        return refs_bibtex, refs_normal

    def format_books_normal(self,books):
        return f"Avain: {books[0]}\nKirjailijan nimi: {books[1]}, {books[2]}\n\
        Otsikko: {books[3]}\nJulkaisuvuosi: {books[4]}\nJulkaisija: {books[5]}".split('\n')

    def format_books_bibtex(self,book):
        return f'@book{{{book[0]}, author = \"{book[2] + " " + book[1]}\", title = \"{book[3]}\", \
            publisher = \"{book[5]}\", year = {book[4]}}}'

    def format_websites_normal(self,websites):
        return f"Avain: {websites[0]}\nTekijä: {websites[2]}, {websites[3]}\n\
        Otsikko: {websites[4]}\nJulkaisuvuosi: {websites[7]}\nUrl: {websites[6]}".split('\n')

    def format_websites_bibtex(self,website):
        return f'@misc{{{website[0]}, title = \"{website[1]}\", author = \"{{{website[2]}\
            + " " + {website[3]}}}\", howpublished = \"url{{{website[6]}}}\", year = {website[7]}"}}'

    def check_if_all_str_book_columns_are_not_empty(self, keyword,
                        author_surname, author_name, title, publisher):
        keyword = keyword.strip()
        author_surname = author_surname.strip()
        author_name = author_name.strip()
        title = title.strip()
        publisher = publisher.strip()

        if len(keyword) < 1 or len(author_surname) < 1 or len(author_name) < 1\
            or len(title) < 1 or len(publisher) < 1:
            return False
        return True

    def check_if_year_is_integer_and_not_empty(self, year):
        year = str(year)
        if any(c.isalpha() for c in year):
            return True
        return False

    def create_new_book_reference(self, reference_id, keyword,
                            author_surname, author_name, title, year, publisher):
        if self.check_if_all_str_book_columns_are_not_empty(keyword,
                            author_surname, author_name, title, publisher):
            if not self.check_if_year_is_integer_and_not_empty(year):
                return self.viitteet.create_new_book_reference(reference_id, keyword,
                                    author_surname, author_name, title, year, publisher)

    def create_new_website_reference(self, reference_id, keyword,
                            author_surname, author_name, title, year, added_at, description, url):
        if not self.check_if_year_is_integer_and_not_empty(year):
            return self.viitteet.create_new_website_reference(reference_id, keyword,added_at,
                                    author_surname, author_name, title, description, url, year)

    def remove_reference(self, keyword):
        book_id = self.viitteet.get_book_by_keyword(keyword)
        website_id = self.viitteet.get_website_by_keyword(keyword)
        if book_id:
            self.viitteet.remove_book_reference(book_id[0])
            self.viitteet.remove_reference(book_id[0])
        if website_id:
            self.viitteet.remove_website_reference(website_id[0])
            self.viitteet.remove_reference(website_id[0])

    def create_website_reference(self, reference_id, keyword,
        added_at, author_surname, author_name, title, description, url, year):
        return self.viitteet.create_website_reference(reference_id, keyword,
        added_at, author_surname, author_name, title, description, url, year)

    def get_all_websites(self):
        return self.viitteet.fetch_websites()
