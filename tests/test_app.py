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


def test_create_book(client):
    response = client.post("/books", json={
        "title": "Test Book",
        "author": "Test Author"
    })

    assert response.status_code == 201

    data = response.get_json()

    assert data["title"] == "Test Book"
    assert data["author"] == "Test Author"


def test_validation_error(client):
    response = client.post("/books", json={
        "title": "Missing Author"
    })

    assert response.status_code == 400


def test_health(client):
    response = client.get("/health")

    assert response.status_code == 200