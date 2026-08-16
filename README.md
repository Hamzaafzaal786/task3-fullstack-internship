# Task 3: Full Stack Development Internship

Complete implementation of **Task 3**, covering FastAPI, Flask, Django background services, Celery, Redis, and scheduled jobs.

## 📁 Structure

* `fastapi-app/` — FastAPI CRUD API
* `flask-app/` — Flask CRUD API
* `background-services/` — FastAPI, Flask & Django background tasks
* `docs/` — Technical report
* `README.md` — Project documentation

## 🚀 Tech Stack

**FastAPI · Flask · Django · SQLAlchemy · Pydantic · Marshmallow · Celery · Redis · APScheduler · Uvicorn**

## 🔧 Quick Start

```bash
git clone https://github.com/YOUR_USERNAME/task3-fullstack-internship.git
cd task3-fullstack-internship
```

### FastAPI

```bash
cd fastapi-app
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Docs: `http://localhost:8000/docs`

### Flask

```bash
cd flask-app
pip install -r requirements.txt
python run.py
```

Docs: `http://localhost:5000/docs`

### Background Services

Requires **Redis** and **Celery** for queued tasks.

## 🧪 CRUD Endpoints

* `POST /items/` — Create
* `GET /items/` — List
* `GET /items/{id}` — Retrieve
* `PUT /items/{id}` — Update
* `DELETE /items/{id}` — Delete

## 📚 Documentation

Includes architecture, implementation, framework comparison, results, challenges, and future improvements.

## 👥 Contributors

* **Developer:** Syed Hamza Afzaal
* **Supervisor:** Alina Baber

## 📌 Status

**Version:** 1.0
**Status:** Complete ✅
**Purpose:** Educational internship project

