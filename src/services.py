import reference.ref as ref

class ReferenceService:
    def __init__(self, ref):
        self.reference = ref

    def get_references_normal(self):
        return self.reference.get_references_normal()

    def create_reference(self):
        pass

    def create_book_reference(self, values: dict) -> bool:
        reference_id = self.reference.create_reference('kirja')
        return self.reference.create_book_reference(reference_id, 
                values["keyword"], 
                values["author_surname"],
                values["author_name"], 
                values["title"], 
                values["year"], 
                values["publisher"]
                )
        
    

reference_service = ReferenceService(ref)