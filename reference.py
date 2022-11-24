from db import db

def create_reference(type):
    sql = "INSERT INTO reference (type) VALUES (:type) returning id"
    reference_id = db.session.execute(sql,{"type":type})
    db.session.commit()
    return reference_id


def create_book_reference(reference_id, keyword, author, title, year, publisher):
    sql = "INSERT INTO book (reference_id, keyword, author, title, year, publisher) VALUES (:reference_id ,:keyword, :author, :title, :year, :publisher);"
    db.session.execute(sql,{
        "reference_id": reference_id,
        "keyword": keyword, 
        "author":author,
        "title":title,
        "year":year,
        "publisher":publisher
        })
    db.session.commit()
