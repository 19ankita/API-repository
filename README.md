# 🧃 API Repository

Welcome to the **API-repository** — a personal playground of modern API design and development using **Flask** and **FastAPI** frameworks.

This project demonstrates how to build and consume RESTful APIs using Python and SQLite. It's ideal for beginners learning backend development, and for anyone interested in understanding the differences between Flask and FastAPI.

---

## 🚀 Features

- ✅ RESTful API with both **Flask** and **FastAPI**
- 🗃️ Uses **SQLite** as a lightweight, file-based database
- 🧪 Endpoints for:
  - Creating a drink
  - Fetching all drinks
  - Fetching a drink by ID
  - Deleting a drink
- 📬 Tested via **Postman**
- 💡 SQLAlchemy ORM for database models

---

## 📂 Project Structure

```bash
API-repository/
│
├── app/
│   ├── application.py           # Flask-based API
│   ├── application_fastapi.py   # FastAPI version of the same API
│   ├── instance/
│   │   └── drinks.db            # SQLite DB file (auto-created)
│   └── consume_api.py           # (Optional) API consumer script
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Tech Stack

- Python 3.9+
- Flask
- FastAPI
- SQLAlchemy
- SQLite
- Uvicorn (for FastAPI dev server)
- Postman (for testing)

---

## 📌 Setup Instructions

### 🔧 1. Clone the Repository

```bash
git clone https://github.com/19ankita/API-repository.git
cd API-repository/app
```

### 🐍 2. Create & Activate a Virtual Environment

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Unix/Mac:
source venv/bin/activate
```

### 📦 3. Install Dependencies

```bash
pip install -r ../requirements.txt
```

---

## 🚀 Running the Apps

### ▶ Flask App

```bash
flask --app application.py --debug run
```

Visit: `http://127.0.0.1:5000/`

---

### ⚡ FastAPI App

```bash
uvicorn application_fastapi:app --reload
```

Visit Swagger UI: `http://127.0.0.1:8000/docs`

---

## 🔁 API Endpoints (FastAPI & Flask)

| Method | Endpoint             | Description            |
|--------|----------------------|------------------------|
| GET    | `/`                  | Hello World            |
| GET    | `/drinks`            | List all drinks        |
| GET    | `/drinks/{id}`       | Get a drink by ID      |
| POST   | `/drinks`            | Create a new drink     |
| DELETE | `/drinks/{id}`       | Delete a drink         |

---

## 🧠 Learnings & Highlights

- Difference between `from_attributes` vs `model_validate` in Pydantic v2
- How FastAPI handles dependency injection with `Depends(get_db)`
- How to use SQLAlchemy with both frameworks
- Testing APIs with Postman and handling 500/404 errors

---


```

---

Let me know if you want a version with badges, screenshots (Postman / Swagger UI), or hosted demo links!
