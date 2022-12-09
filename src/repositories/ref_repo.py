from db import db

class ReferenceRepository:
    def __init__(self):
        pass

    def create_reference(self, type):
        sql = "INSERT INTO reference (type) VALUES (:type) returning id"
        reference_id = db.session.execute(sql,{"type":type}).fetchone()[0]
        db.session.commit()
        return reference_id

    def create_new_book_reference(self, reference_id, keyword,
                            author_surname, author_name, title, year, publisher):
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

    def create_website_reference(self, reference_id, keyword,
        added_at, author_surname, author_name, title, description, url, year):
        try:
            sql = """INSERT INTO website
            (website_id, keyword, added_at, author_surname, author_name, title, description, url, year)
            VALUES (:website_id ,:keyword, :added_at, :author_surname, :author_name, :title, :description, :url, :year);"""
            db.session.execute(sql,{
            "website_id": reference_id,
            "keyword": keyword,
            "added_at": added_at,
            "author_surname": author_surname,
            "author_name": author_name,
            "title": title,
            "description": description,
            "url": url,
            "year": year
            })
            db.session.commit()
            return True
        except:
            return False

    def empty_books(self):
        sql = "DELETE FROM book"
        db.session.execute(sql)

    def fetch_books(self):
        sql = """SELECT book_id, keyword, author_surname,
        author_name, title, year, publisher FROM book"""
        result = db.session.execute(sql)
        return result.fetchall()

    def get_references_normal(self):
        sql = """SELECT keyword, author_surname, author_name, title, year, publisher from book"""
        result = db.session.execute(sql)
        return result.fetchall()

viiterepositorio = ReferenceRepository()