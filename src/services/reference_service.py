import repositories.ref_repo as refe

class ReferenceService:
    def __init__(self, viiterepo=refe.viiterepositorio):
        self.viitteet = viiterepo

    def get_all_references(self):
        return self.viitteet.get_references_normal()

    def get_all_books(self):
        return self.viitteet.fetch_books()

    def remove_all_books(self):
        self.viitteet.empty_books()

    def create_reference(self, ref_type):
        return self.viitteet.create_reference(ref_type)

    def create_new_book_reference(self, reference_id, keyword,
                            author_surname, author_name, title, year, publisher):
        return self.viitteet.create_new_book_reference(reference_id, keyword,
                            author_surname, author_name, title, year, publisher)

    def remove_reference(self, keyword):
        book_id = self.viitteet.get_book_by_keyword(keyword)
        website_id = self.viitteet.get_website_by_keyword(keyword)
        if book_id:
            self.viitteet.remove_book_reference(book_id[0])
            self.viitteet.remove_reference(book_id[0])
        if website_id:
            self.viitteet.remove_website_reference(website_id[0])
            self.viitteet.remove_reference(website_id[0])


    def delete_website(self, website_id):
        pass


