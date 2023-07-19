from flask import Flask as FlaskApi
from flask import request, jsonify
from collection import collection

app = FlaskApi(__name__)

app.config["DEBUG"] = True  

@app.get("/api")
def index():
    return jsonify({"collection": collection})

@app.get("/api/books/")
def get_all_books():
    return jsonify({"collection": collection})

@app.get("/api/book/<string:author>")
def get_book_by_author(author):
    books = [book for book in collection if book['author'].lower() == author.lower() ]

    if not books:
        return jsonify({"message": "We cannot find book with given author."}), 404
    
    return jsonify({"books": books})

if __name__ == "__main__":
    app.run()