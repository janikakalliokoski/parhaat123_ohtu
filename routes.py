from app import app
from flask import render_template, request, redirect, flash
import reference

@app.route("/", methods=["GET", "POST"])
def main():
    if request.method =="GET":
        return render_template("main.html")

    if request.method == "POST":
        keyword = request.form.get("keyword", "").strip()
        author = request.form.get("author", "").strip()
        title = request.form.get("title", "").strip()
        year = request.form.get("year", "").strip()
        publisher = request.form.get("publisher", "").strip()
        reference_id = reference.create_reference('kirja')

        if reference.create_book_reference(reference_id,keyword, author, title, year, publisher):
            return render_template("main.html",
                                    message="Viite luotu onnistuneesti!")
        else:
            return render_template("main.html", ermsg="kokeile toista avainsanaa")
    return render_template("main.html")
