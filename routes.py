from app import app
from flask import render_template, request, redirect

@app.route("/")
def main():
    return render_template("main.html")