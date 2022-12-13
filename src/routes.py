from flask import render_template, request, redirect, flash
from app import app
import services.reference_service as refer
#from services.reference_service import ReferenceService

@app.route("/", methods=["GET", "POST"])
def main():
    # from ref.ref import Reference as ref
    service = refer.ReferenceService()
    if request.method =="GET":
        refs_bibtex, refs_normal = service.get_references()
        return render_template("main.html", refs_bibtex=refs_bibtex,refs_normal=refs_normal)

    if request.method == "POST":
        service = refer.ReferenceService()
        keyword = request.form.get("keyword", "").strip()
        author_surname = request.form.get("author_surname", "").strip()
        author_name = request.form.get("author_name", "").strip()
        title = request.form.get("title", "").strip()
        year = request.form.get("year", "").strip()
        publisher = request.form.get("publisher", "").strip()
        tag = request.form.get("tag", "").strip()
        description = request.form.get("description", "").strip()
        added_at = request.form.get("added_at", "").strip()
        url = request.form.get("url", "").strip()

        if url:
            reference_id = service.create_new_reference('verkkosivu')
            if service.create_new_website_reference(reference_id,keyword,author_surname,
                author_name, title, year, added_at, description, url, tag):
                refs_bibtex, refs_normal = service.get_references()
                return render_template("main.html",
                                        message="Viite luotu onnistuneesti!",
                                        refs_bibtex=refs_bibtex,
                                        refs_normal=refs_normal)
        if publisher:
            reference_id = service.create_reference('kirja')
            if service.create_new_book_reference(reference_id, keyword, author_surname,
                                        author_name, title, year, publisher, tag):
                refs_bibtex, refs_normal = service.get_references()
                return render_template("main.html",
                                        message="Viite luotu onnistuneesti!",
                                        refs_bibtex=refs_bibtex,
                                        refs_normal=refs_normal
                                    )
        return render_template("main.html",
                                message="Viitteen luonti ei onnistunut, kokeile toista avainta")
    return None

@app.route("/delete", methods=["POST"])
def delete():
    service = refer.ReferenceService()
    if request.method == "POST":
        keyword = request.form.get("keyword", "").strip()
        service.remove_reference(keyword)
        return redirect('/') 

@app.route("/listTag", methods=["POST"])
def list_by_tag():
    service = refer.ReferenceService()
    tag = request.form["tag"]

    try:
        books_bib, books_tag = service.get_tag_references_book(tag)
        websites_bib, websites_tag = service.get_tag_references_website(tag)
        tagged_bibtex = books_bib + websites_bib
        tagged_normal = books_tag + websites_tag
        return render_template("tags.html", tagged_bibtex = tagged_bibtex, tagged_normal = tagged_normal)
    except:
        return render_template("tags.html",
                                message="Viitteitä ei löytynyt kyseisellä tagilla")

