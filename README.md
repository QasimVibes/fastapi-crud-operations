# FastAPI Student Management App

## Overview
This repository contains a FastAPI application for managing a global list of students in memory. The objective of this assignment is to create a RESTful API using FastAPI to perform CRUD operations on student data.

## Functionality
- Create a global list of students stored in memory.
- Implement CRUD operations (Create, Read, Update, Delete) for students:
    - `GET /students`: Retrieve all students.
    - `GET /students/{student_id}`: Retrieve specific student details.
    - `POST /students`: Add a new student.
    - `PUT /students/{student_id}`: Update a student's details.
    - `DELETE /students/{student_id}`: Delete a student.

## Technology Stack
- Python
- FastAPI

## Student Data Schema
Each student object should have the following attributes:
- Student ID (unique)
- Name
- Age
- Grade/Class

## Setup Instructions

### Prerequisites
- Python 3.7 or higher
- Poetry package manager

### Steps
1. **Clone the repository:**
    ```bash
    git clone: https://github.com/QasimVibes/fastapi-crud-operations.git
    ```

2. **Install project dependencies using Poetry:**
    ```bash
    poetry install
    ```

3. **Run the FastAPI application:**
    ```bash
    poetry run dev
    ```

    This command will start the FastAPI application locally. The `--reload` option enables automatic reloading of the server when changes are made to the source code.

4. **Access the API documentation:**
    Once the application is running, you can access the API documentation by visiting [http://localhost:8080/docs](http://localhost:8080/docs) in your web browser. This interactive documentation is generated automatically by FastAPI and provides details about the available endpoints, request/response schemas, and allows you to test the API endpoints directly from the browser.

## Notes
- Ensure that you follow best practices for secure and efficient API development.
- For deployment, consider using ASGI servers like Uvicorn behind a production-ready web server like Nginx or Gunicorn.
- FastAPI offers built-in support for data validation, serialization, and automatic OpenAPI documentation generation, which can significantly speed up API development.
- Explore FastAPI's extensive documentation for advanced features and usage patterns: [FastAPI Documentation](https://fastapi.tiangolo.com/).
