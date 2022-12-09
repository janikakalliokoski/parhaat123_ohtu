from db import db

class Reference:
    def create_reference(type):
        sql = "INSERT INTO reference (type) VALUES (:type) returning id"
        reference_id = db.session.execute(sql,{"type":type}).fetchone()[0]
        db.session.commit()
        return reference_id

    def create_book_reference(reference_id, keyword,
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

    def create_website_reference(reference_id, keyword,
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

    def empty_books():
        sql = "DELETE FROM book"
        db.session.execute(sql)

    def fetch_books():
        sql = """SELECT book_id, keyword, author_surname,
        author_name, title, year, publisher FROM book"""
        result = db.session.execute(sql)
        return result.fetchall()
    
    def fetch_websites():
        sql = """SELECT website_id, keyword, author_surname,
        author_name, title, year, url FROM website"""
        result = db.session.execute(sql)
        return result.fetchall()
    
    def remove_book(id):
        sql = """DELETE FROM book WHERE book_id={id}"""
        result = db.session.execute(sql)
        return result.fetchall()

    def remove_website(id):
        sql = """DELETE FROM website WHERE website_id={id}"""
        result = db.session.execute(sql)
        return result.fetchall()

    def get_references_normal():
        sql = """SELECT keyword, author_surname, author_name, title, year, publisher from book"""
        result = db.session.execute(sql)
        return result.fetchall()
