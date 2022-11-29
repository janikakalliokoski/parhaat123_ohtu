from flask import render_template, request, redirect
from app import app
import reference

@app.route("/", methods=["GET", "POST"])
def main():
    if request.method =="GET":
        print("get")
        return render_template("main.html")
    print("post")
    keyword = request.form.get("keyword", "").strip()
    author = request.form.get("author", "").strip()
    title = request.form.get("title", "").strip()
    year = request.form.get("year", "").strip()
    publisher = request.form.get("publisher", "").strip()
    print(publisher)
    reference_id = reference.create_reference('kirja')
    print(reference_id)
    reference.create_book_reference(reference_id,keyword, author, title, year, publisher)
    return render_template("main.html")
