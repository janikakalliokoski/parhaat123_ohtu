from flask import render_template, request, redirect, flash
from app import app
import services.reference_service as refer
#from services.reference_service import ReferenceService

@app.route("/", methods=["GET", "POST"])
def main():
    # from ref.ref import Reference as ref
    service = refer.ReferenceService()
    if request.method =="GET":
        return render_template("main.html", refs=service.get_all_references())

    if request.method == "POST":
        service = refer.ReferenceService()
        keyword = request.form.get("keyword", "").strip()
        author_surname = request.form.get("author_surname", "").strip()
        author_name = request.form.get("author_name", "").strip()
        title = request.form.get("title", "").strip()
        year = request.form.get("year", "").strip()
        publisher = request.form.get("publisher", "").strip()
        tag = request.form.get("tag", "").strip()
        reference_id = service.create_reference('kirja')

        if service.create_new_book_reference(reference_id, keyword, author_surname,
                                    author_name, title, year, publisher, tag):
            return render_template("main.html",
                                    message="Viite luotu onnistuneesti!",
                                    refs=service.get_all_references())
        return render_template("main.html",
                                message="Viitteen luonti ei onnistunut, kokeile toista avainta")
    return None

@app.route("/delete", methods=["POST"])
def delete():
    service = refer.ReferenceService()
    if request.method == "POST":
        keyword = request.form.get("keyword", "").strip()
        service.remove_reference(keyword)
        return render_template("main.html",
                                message="Viite poistettu onnistuneesti!",
                                refs=service.get_all_references())

@app.route("/listTag", methods=["POST"])
def list_by_tag():
    service = refer.ReferenceService()
    tag = request.form["tag"]

    books_tags = service.get_books_by_tags(tag)
    website_tags = service.get_websites_by_tag(tag)

    return render_template("tags.html", book_list=books_tags, misc_list=website_tags)
