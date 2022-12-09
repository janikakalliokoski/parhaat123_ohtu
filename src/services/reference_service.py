from reference.ref import viiterepositorio as default_viiterepo

class ReferenceService:
    def __init__(self, viiterepo=default_viiterepo):
        self.viitteet = viiterepo

    def get_all_references(self):
        return self.viitteet.get_references_normal()

    def get_all_books(self):
        return self.viitteet.fetch_books()

    def remove_all_books(self):
        self.viitteet.empty_books()

    def create_reference(self, ref_type):
        return self.viitteet.create_reference(ref_type)

    def create_book_reference(self, reference_id, keyword,
                            author_surname, author_name, title, year, publisher):
        return self.viitteet.create_book_reference(reference_id, keyword,
                            author_surname, author_name, title, year, publisher)

service = ReferenceService()
