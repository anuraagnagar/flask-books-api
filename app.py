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

if __name__ == "__main__":
    app.run()