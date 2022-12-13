from unittest import result
from db import db

class ReferenceRepository:
    def __init__(self):
        pass

    def create_new_reference(self, type):
        sql = "INSERT INTO reference (type) VALUES (:type) returning id"
        reference_id = db.session.execute(sql,{"type":type}).fetchone()[0]
        db.session.commit()
        return reference_id

    def create_new_book_reference(self, reference_id, keyword,
                            author_surname, author_name, title, year, publisher, tag):
        try:
            sql = """INSERT INTO book
                    (book_id, keyword, author_surname, author_name, title, year, publisher, tag)
                    VALUES (:book_id ,:keyword, :author_surname,
                    :author_name, :title, :year, :publisher, :tag);"""
            db.session.execute(sql,{
                "book_id": reference_id,
                "keyword": keyword,
                "author_surname":author_surname,
                "author_name": author_name,
                "title":title,
                "year":year,
                "publisher":publisher,
                "tag":tag
                })
            db.session.commit()
            return True
        except:
            return False

    def create_new_website_reference(self, reference_id, keyword,
        added_at, author_surname, author_name, title, description, url, year, tag):
        try:
            sql = """INSERT INTO website
            (website_id, keyword, added_at, author_surname, author_name, title, description, url, year, tag)
            VALUES (:website_id ,:keyword, :added_at,
            :author_surname, :author_name, :title, :description, :url, :year, :tag);"""
            db.session.execute(sql,{
            "website_id": reference_id,
            "keyword": keyword,
            "added_at": added_at,
            "author_surname": author_surname,
            "author_name": author_name,
            "title": title,
            "description": description,
            "url": url,
            "year": year,
            "tag": tag
            })
            db.session.commit()
            return True
        except:
            return False

    def remove_all_books(self):
        sql = "DELETE FROM book;"
        db.session.execute(sql)

    def fetch_books(self):
        sql = """SELECT book_id, keyword, author_surname,
        author_name, title, year, publisher FROM book;"""
        result = db.session.execute(sql)
        return result.fetchall()

    def get_book_by_keyword(self, keyword):
        sql = """SELECT book_id FROM book WHERE keyword=:keyword;"""
        result = db.session.execute(sql, {"keyword":keyword})
        return result.fetchone()

    def get_website_by_keyword(self, keyword):
        sql = """SELECT website_id FROM website WHERE keyword=:keyword;"""
        result = db.session.execute(sql, {"keyword":keyword})
        return result.fetchone()

    def remove_reference(self, reference_id):
        sql = """ DELETE from reference WHERE id=:id;"""
        db.session.execute(sql, {"id":reference_id})
        db.session.commit()

    def remove_book_reference(self, book_id):
        sql = """ DELETE from book WHERE book_id=:id;"""
        db.session.execute(sql, {"id":book_id})
        db.session.commit()

    def remove_website_reference(self, web_id):
        sql = """ DELETE from website WHERE website_id=:id;"""
        db.session.execute(sql, {"id":web_id})
        db.session.commit()

    def get_book_references_normal(self):
        sql = """SELECT keyword, author_surname, author_name, title,
        year, publisher, tag from book;"""
        result = db.session.execute(sql)
        return result.fetchall()

    def get_book_references_tag(self, tag):
        sql = """SELECT keyword, author_surname, author_name, title, year,
         publisher, tag from book WHERE tag=:tag;"""
        result = db.session.execute(sql, {"tag":tag})
        return result.fetchall()

    def get_website_references_normal(self):
        sql = """SELECT keyword, added_at, author_surname, author_name,
        title, description, url, year, publisher, tag from website;"""
        result = db.session.execute(sql)
        return result.fetchall()

    def get_website_references_tag(self, tag):
        sql = """SELECT keyword, added_at, author_surname, author_name,
        title, description, url, year, publisher, tag from website WHERE tag=:tag;"""
        result = db.session.execute(sql, {"tag":tag})
        return result.fetchall()

    def get_all_references(self):
        sql = """select * from reference;"""
        result = db.session.execute(sql)
        return result.fetchall()

    def fetch_websites(self):
        pass

    def remove_all_websites(self):
        pass

viiterepositorio = ReferenceRepository()
