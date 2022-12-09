from flask import render_template, request, redirect, flash
from app import app
import services.reference_service as refer
#from services.reference_service import ReferenceService

@app.route("/", methods=["GET", "POST"])
def main():
    # from ref.ref import Reference as ref
    r = refer.ReferenceService()
    if request.method =="GET":
        return render_template("main.html", refs=r.get_all_references())

    if request.method == "POST":
        r = refer.ReferenceService()
        keyword = request.form.get("keyword", "").strip()
        author_surname = request.form.get("author_surname", "").strip()
        author_name = request.form.get("author_name", "").strip()
        title = request.form.get("title", "").strip()
        year = request.form.get("year", "").strip()
        publisher = request.form.get("publisher", "").strip()
        reference_id = r.create_reference('kirja')

        if r.create_new_book_reference(reference_id, keyword, author_surname,
                                    author_name, title, year, publisher):
            return render_template("main.html",
                                    message="Viite luotu onnistuneesti!",
                                    refs=r.get_all_references())
        return render_template("main.html",
                                message="Viitteen luonti ei onnistunut, kokeile toista avainta")
    return None

@app.route("/delete", methods=["POST"])
def delete():
    r = refer.ReferenceService()
    if request.method == "POST":
        keyword = request.form.get("keyword", "").strip()
        r.remove_reference(keyword)
        return redirect("/")

