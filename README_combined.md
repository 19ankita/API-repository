
# 🧃 API Repository — FastAPI + Flask Mini Projects

Welcome to **API-repository**, a collection of mini REST API projects built with FastAPI and Flask.  
Each sub-project is self-contained and demonstrates CRUD operations using either SQLite or in-memory data.

---

## 📁 Folder Structure

```bash
API-repository/
└── app/
    ├── application.py             # Flask Drink API
    ├── application_fastapi.py     # FastAPI Drink API
    ├── main.py                    # FastAPI Comment/Post API
    └── instance/
        └── drinks.db              # SQLite DB (auto-created)
```

---

## 🧪 1. FastAPI Drink API (`application_fastapi.py`)

A RESTful API to manage drinks (like beverages) using **FastAPI**, **SQLite**, and **SQLAlchemy**.

### ▶ Features

- CRUD for `Drink` model
- Uses SQLite (database stored in `instance/drinks.db`)
- Auto-generated Swagger UI

### 🔗 Endpoints

| Method | Route             | Description         |
|--------|-------------------|---------------------|
| GET    | `/drinks`         | List all drinks     |
| GET    | `/drinks/{id}`    | Get drink by ID     |
| POST   | `/drinks`         | Create a new drink  |
| DELETE | `/drinks/{id}`    | Delete a drink      |

### 🔧 Run

```bash
uvicorn application_fastapi:app --reload
```

---

## 💬 2. FastAPI Post API (`main.py`)

A basic blog-like post API using FastAPI with in-memory data (no database).

### ▶ Features

- CRUD for blog-style posts
- Uses Pydantic for validation
- Built-in examples for Swagger UI
- Great for beginners learning FastAPI request/response handling

### 🔗 Endpoints

| Method | Route               | Description         |
|--------|---------------------|---------------------|
| GET    | `/posts`            | Get all posts       |
| GET    | `/posts/{id}`       | Get post by ID      |
| GET    | `/posts/latest`     | Get latest post     |
| POST   | `/posts`            | Create a new post   |
| PUT    | `/posts/{id}`       | Update a post       |
| DELETE | `/posts/{id}`       | Delete a post       |

### 🔧 Run

```bash
uvicorn main:app --reload
```
Visit Swagger UI: http://127.0.0.1:8000/docs

---

## 🧠 Use Case & Learning Goals

| Project        | Focus                                      |
|----------------|---------------------------------------------|
| Drink API      | Full stack: DB + SQLAlchemy + CRUD          |
| Post API       | FastAPI basics + in-memory + Swagger usage  |

---

