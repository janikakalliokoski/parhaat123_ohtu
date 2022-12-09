from flask import render_template, request, redirect, flash
from app import app
from services.reference_service import service

@app.route("/", methods=["GET", "POST"])
def main():
    # from ref.ref import Reference as ref
    if request.method =="GET":
        return render_template("main.html", refs=service.get_all_references())
        print(refs)

    if request.method == "POST":
        keyword = request.form.get("keyword", "").strip()
        author_surname = request.form.get("author_surname", "").strip()
        author_name = request.form.get("author_name", "").strip()
        title = request.form.get("title", "").strip()
        year = request.form.get("year", "").strip()
        publisher = request.form.get("publisher", "").strip()
        reference_id = service.create_reference('kirja')

        if service.create_book_reference(reference_id, keyword, author_surname,
                                    author_name, title, year, publisher):
            return render_template("main.html",
                                    message="Viite luotu onnistuneesti!",
                                    refs=service.get_all_references())
        return render_template("main.html",
                                message="Viitteen luonti ei onnistunut, kokeile toista avainta")
    return None

@app.route("/delete", methods=["POST"])
def delete():
    if request.method == "POST":
        keyword = request.form.get("keyword", "").strip()
        service.remove_reference(keyword)
        return redirect("/")

