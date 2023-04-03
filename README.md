# Django Todo App with REST API
This is a simple todo app built using Django and Django REST framework. The app provides a RESTful API that allows you to perform CRUD (Create, Read, Update, Delete) operations on todo items.

## Features
- Add new todo items with a title and description
- Mark todo items as complete
- Edit existing todo items
- Delete todo items
- Retrieve a list of all todo items

## Requirements
- Python 3.6 or higher
- Django 3.2 or higher
- Django REST framework 3.12 or higher
## Installation
1. Clone the repository:
```bash

git clone https://github.com/your_username/todo-app.git

```
2. Create a virtual environment and activate it:
```bash

python3 -m venv env
source env/bin/activate
```
3. Install the required packages:
```
pip install -r requirements.txt
```
4. Run database migrations:
```
python manage.py migrate
```
5. Start the development server:
```
python manage.py runserver
```
6. Access the app at http://localhost:8000/.
## API Endpoints
- **GET /api/todos/**: Retrieve a list of all todo items.
- **POST /api/todos/**: Add a new todo item.
- **GET /api/todos/{id}/**: Retrieve a single todo item by ID.
- **PUT /api/todos/{id}/**: Update a todo item.
- **DELETE /api/todos/{id}/**: Delete a todo item.
