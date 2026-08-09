# Readify Bookstore API

Readify Bookstore API is a RESTful API built with Python and Flask for managing books and authors.

The project includes RESTful endpoints, validation, automated testing, OpenAPI documentation, logging, health monitoring, and a GitHub Actions CI/CD pipeline.

## Features

- RESTful API design
- Book CRUD operations
- Author listing
- Proper HTTP methods and status codes
- Input validation
- OpenAPI documentation
- Automated pytest testing
- Automated Postman testing
- GitHub Actions CI/CD
- Request logging
- Health monitoring endpoint

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/books` | List all books |
| POST | `/books` | Create a new book |
| GET | `/books/{id}` | Retrieve a book by ID |
| PUT | `/books/{id}` | Replace/update a book |
| PATCH | `/books/{id}` | Partially update a book |
| DELETE | `/books/{id}` | Delete a book |
| GET | `/authors` | List all authors |
| GET | `/health` | Check API health |

## HTTP Status Codes

The API uses standard HTTP status codes.

- `200 OK` - Request completed successfully
- `201 Created` - New book created successfully
- `400 Bad Request` - Missing or invalid required data
- `404 Not Found` - Requested book does not exist

## Installation

Clone the repository:

```bash
git clone https://github.com/ouladsaiady/readify-bookstore-api.git
