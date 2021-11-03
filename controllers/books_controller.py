from flask import Flask, render_template, redirect, request, Blueprint

from repositories import author_repository
from repositories import book_repository

books_blueprint = Blueprint("books", __name__)

@books_blueprint.route("/books")
def books():
    all_books = book_repository.select_all()
    return render_template("books/index.html", all_books=all_books)

@books_blueprint.route("/books/<id>/delete", methods=["POST"])
def delete_book(id):
    book_repository.delete(id)
    return redirect("/books")

@books_blueprint.route("/books/new")
def get_new():
    return render_template("books/new.html")

@books_blueprint.route("/books/new", methods=["POST"])
def add_book():
    title = request.form["title"]
    author_id = request.form["author"]
    author = author_repository.select(author_id)
    book = Book(title, author)
    book_repository.save(book)
    return redirect("/books")
