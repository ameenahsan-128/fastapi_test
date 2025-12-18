# FastAPI User Profile API

A simple FastAPI application that provides an API endpoint to insert user profiles into a MongoDB database.

## Features

- **FastAPI Framework**: Modern, fast web framework for building APIs
- **MongoDB Integration**: Stores user profile data in MongoDB
- **Pydantic Validation**: Automatic request validation using Pydantic models
- **RESTful API**: Clean POST endpoint for user profile creation

## Prerequisites

Before running this application, ensure you have the following installed:

- Python 3.7+
- MongoDB (running locally on default port 27017)
- pip (Python package manager)

## Installation

1. Clone this repository or navigate to the project directory:
```bash
cd /home/expertz/test
```

2. Install required dependencies:
```bash
pip install fastapi pymongo pydantic uvicorn
```

## Configuration

The application is configured to connect to MongoDB with the following settings:

- **MongoDB URL**: `mongodb://localhost:27017`
- **Database Name**: `users`
- **Collection Name**: `users`

You can modify these settings in `main.py` if needed.

## Usage

### Starting the Server

Run the application using uvicorn:

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

### API Endpoints

#### Create User Profile

**Endpoint**: `POST /`

**Request Body**:
```json
{
  "name": "John Doe",
  "email": "john.doe@example.com",
  "message": "Hello, this is my profile!"
}
```

**Response**:
```json
{
  "_id": "507f1f77bcf86cd799439011",
  "name": "John Doe",
  "email": "john.doe@example.com",
  "message": "Hello, this is my profile!"
}
```

### Testing the API

You can test the API using curl:

```bash
curl -X POST "http://localhost:8000/" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "email": "john.doe@example.com",
    "message": "Hello, this is my profile!"
  }'
```

Or visit the interactive API documentation at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Project Structure

```
.
├── main.py          # Main application file
├── README.md        # This file
└── __pycache__/     # Python cache directory
```

## Data Model

### Profile

| Field   | Type   | Required | Description                    |
|---------|--------|----------|--------------------------------|
| name    | string | Yes      | User's full name               |
| email   | string | Yes      | User's email address           |
| message | string | Yes      | User's profile message         |

## Dependencies

- **fastapi**: Web framework for building APIs
- **pymongo**: MongoDB driver for Python
- **pydantic**: Data validation using Python type annotations
- **uvicorn**: ASGI server for running FastAPI applications

## Development

To run the application in development mode with auto-reload:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## License

This project is open source and available for educational purposes.

## Author

Created on 2025-12-18
