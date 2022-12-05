from db import db

class Reference:
    def create_reference(type):
        sql = "INSERT INTO reference (type) VALUES (:type) returning id"
        reference_id = db.session.execute(sql,{"type":type}).fetchone()[0]
        db.session.commit()
        return reference_id

    def create_book_reference(reference_id, keyword, author_surname, author_name, title, year, publisher):
        try:
            sql = """INSERT INTO book
                    (book_id, keyword, author_surname, author_name, title, year, publisher)
                    VALUES (:book_id ,:keyword, :author_surname, :author_name, :title, :year, :publisher);"""
            db.session.execute(sql,{
                "book_id": reference_id,
                "keyword": keyword,
                "author_surname":author_surname,
                "author_name": author_name,
                "title":title,
                "year":year,
                "publisher":publisher
                })
            db.session.commit()
            return True
        except:
            return False

    def books_amount():
        sql = "SELECT COUNT(*) FROM book"
        result = db.session.execute(sql)

        return result.fetchone()

    def get_references_normal():
        sql = "select keyword, author_surname, author_name, title, year, publisher from book"
        result = db.session.execute(sql)

        return result.fetchall()

    def get_references_bib():
        pass
