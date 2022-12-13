import repositories.ref_repo as refe

class ReferenceService:
    def __init__(self, viiterepo=refe.viiterepositorio):
        self.viitteet = viiterepo

    def get_all_references(self):
        return self.viitteet.get_book_references_normal()

    def get_all_books(self):
        return self.viitteet.fetch_books()

    def remove_all_books(self):
        self.viitteet.remove_all_books()

    def create_reference(self, ref_type):
        return self.viitteet.create_reference(ref_type)
    
    def get_books_by_tags(self,tag):
        return self.viitteet.get_book_by_tag(tag)
    
    def get_websites_by_tag(self,tag):
        return self.viitteet.get_website_by_tag(tag)

    def check_if_all_str_book_columns_are_not_empty(self, keyword,
                        author_surname, author_name, title, publisher, tag):
        keyword = keyword.strip()
        author_surname = author_surname.strip()
        author_name = author_name.strip()
        title = title.strip()
        publisher = publisher.strip()
        tag = tag.strip()

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
                            author_surname, author_name, title, year, publisher, tag):
        if self.check_if_all_str_book_columns_are_not_empty(keyword,
                            author_surname, author_name, title, publisher, tag):
            if not self.check_if_year_is_integer_and_not_empty(year):
                return self.viitteet.create_new_book_reference(reference_id, keyword,
                                    author_surname, author_name, title, year, publisher, tag)

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
        added_at, author_surname, author_name, title, description, url, year, tag):
        return self.viitteet.create_website_reference(reference_id, keyword,
        added_at, author_surname, author_name, title, description, url, year)

    def get_all_websites(self):
        return self.viitteet.fetch_websites()
