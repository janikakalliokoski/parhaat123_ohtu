from db import db

def create_reference(type):
    sql = "INSERT INTO reference (type) VALUES (:type) returning id"
    reference_id = db.session.execute(sql,{"type":type}).fetchone()[0]
    db.session.commit()
    return reference_id


def create_book_reference(reference_id, keyword, author, title, year, publisher):
    sql = "INSERT INTO book (book_id, keyword, author, title, year, publisher) VALUES (:book_id ,:keyword, :author, :title, :year, :publisher);"
    db.session.execute(sql,{
        "book_id": reference_id,
        "keyword": keyword, 
        "author":author,
        "title":title,
        "year":year,
        "publisher":publisher
        })
    db.session.commit()
