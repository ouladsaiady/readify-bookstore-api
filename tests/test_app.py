import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_get_books(client):
    response = client.get("/books")
    assert response.status_code == 200


def test_full_book_crud_flow(client):
    # CREATE
    create_response = client.post("/books", json={
        "title": "CRUD Test Book",
        "author": "CRUD Test Author"
    })

    assert create_response.status_code == 201

    created_book = create_response.get_json()
    book_id = created_book["id"]

    assert created_book["title"] == "CRUD Test Book"
    assert created_book["author"] == "CRUD Test Author"

    # RETRIEVE
    get_response = client.get(f"/books/{book_id}")

    assert get_response.status_code == 200

    retrieved_book = get_response.get_json()

    assert retrieved_book["id"] == book_id
    assert retrieved_book["title"] == "CRUD Test Book"

    # UPDATE
    update_response = client.put(f"/books/{book_id}", json={
        "title": "Updated CRUD Test Book",
        "author": "CRUD Test Author"
    })

    assert update_response.status_code == 200

    updated_book = update_response.get_json()

    assert updated_book["title"] == "Updated CRUD Test Book"

    # DELETE
    delete_response = client.delete(f"/books/{book_id}")

    assert delete_response.status_code == 200

    delete_data = delete_response.get_json()

    assert delete_data["message"] == "Book deleted successfully"

    # VERIFY DELETION
    missing_response = client.get(f"/books/{book_id}")

    assert missing_response.status_code == 404


def test_validation_error(client):
    response = client.post("/books", json={
        "title": "Missing Author"
    })

    assert response.status_code == 400

    data = response.get_json()

    assert data["error"] == "Title and author are required"


def test_get_authors(client):
    response = client.get("/authors")

    assert response.status_code == 200


def test_health(client):
    response = client.get("/health")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "healthy"