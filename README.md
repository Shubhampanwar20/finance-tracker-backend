# 💰 Finance Tracker Backend

## 📌 Overview

This project is a backend finance tracking system built using FastAPI and SQLite. It allows users to manage financial transactions, track income and expenses, and generate useful summaries.

The system is designed with clean architecture, proper API design, and structured code to simulate a real-world backend application.

---

## 🚀 Features

* ✅ Create, view, and manage financial transactions
* ✅ Income and expense tracking
* ✅ Summary analytics (total income, expenses, balance)
* ✅ Filtering by type and category
* ✅ REST API with FastAPI
* ✅ SQLite database integration
* ✅ Interactive API documentation (Swagger UI)

---

## 🛠 Tech Stack

* Python
* FastAPI
* SQLAlchemy
* SQLite

---

## ⚙️ Installation & Setup

```bash
git clone https://github.com/yourusername/finance-tracker-backend.git
cd finance-tracker-backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

---

## 📡 API Endpoints

* `POST /transactions` → Create transaction
* `GET /transactions` → Get all transactions
* `GET /summary` → Get financial summary

---

## 📄 API Documentation

Swagger UI available at:
http://127.0.0.1:8000/docs

---

## 🎯 Purpose

This project was developed as part of a backend development assignment to demonstrate:

* Clean Python coding practices
* API design and structure
* Database handling
* Business logic implementation

---

## 📌 Future Improvements

* Authentication (JWT)
* Role-based access control
* Pagination
* Advanced filtering
* Deployment

---
