import logging

from flask import Flask, jsonify, request

app = Flask(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

@app.after_request
def log_request(response):
    app.logger.info(
        "%s %s - %s",
        request.method,
        request.path,
        response.status_code
    )
    return response

books = [
    {
        "id": 1,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald"
    },
    {
        "id": 2,
        "title": "1984",
        "author": "George Orwell"
    }
]

authors = [
    {
        "id": 1,
        "name": "F. Scott Fitzgerald"
    },
    {
        "id": 2,
        "name": "George Orwell"
    }
]

@app.route("/authors", methods=["GET"])
def get_authors():
    return jsonify(authors), 200


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Welcome to the Readify Bookstore API"
    }), 200


@app.route("/books", methods=["GET"])
def get_books():
    return jsonify(books), 200

@app.route("/books/<int:id>", methods=["GET"])
def get_book(id):
    for book in books:
        if book["id"] == id:
            return jsonify(book), 200

    return jsonify({
        "error": "Book not found"
    }), 404

@app.route("/books", methods=["POST"])
def create_book():
    data = request.get_json()

    if not data or "title" not in data or "author" not in data:
        return jsonify({
            "error": "Title and author are required"
        }), 400

    new_book = {
        "id": len(books) + 1,
        "title": data["title"],
        "author": data["author"]
    }

    books.append(new_book)

    return jsonify(new_book), 201

@app.route("/books/<int:id>", methods=["PUT"])
def update_book(id):
    data = request.get_json()

    if not data or "title" not in data or "author" not in data:
        return jsonify({
            "error": "Title and author are required"
        }), 400

    for book in books:
        if book["id"] == id:
            book["title"] = data["title"]
            book["author"] = data["author"]

            return jsonify(book), 200

    return jsonify({
        "error": "Book not found"
    }), 404
    
@app.route("/books/<int:id>", methods=["PATCH"])
def patch_book(id):
    data = request.get_json()

    for book in books:
        if book["id"] == id:
            if "title" in data:
                book["title"] = data["title"]

            if "author" in data:
                book["author"] = data["author"]

            return jsonify(book), 200

    return jsonify({
        "error": "Book not found"
    }), 404

@app.route("/books/<int:id>", methods=["DELETE"])
def delete_book(id):
    for book in books:
        if book["id"] == id:
            books.remove(book)
            return jsonify({
                "message": "Book deleted successfully"
            }), 200

    return jsonify({
        "error": "Book not found"
    }), 404

@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy"
    }), 200

if __name__ == "__main__":
    app.run(debug=True)