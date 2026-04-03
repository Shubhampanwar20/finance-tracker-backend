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
* Pydantic

---

## ⚙️ Installation & Setup

```bash
git clone https://github.com/Shubhampanwar20/finance-tracker-backend.git
cd finance-tracker-backend

python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

pip install -r requirements.txt

uvicorn app.main:app --reload
```

---

## 📡 API Endpoints

* `POST /transactions` → Create a transaction
* `GET /transactions` → Get all transactions
* `GET /summary` → Get financial summary

---

## 📊 Sample Response

```json
{
  "total_income": 6000,
  "total_expense": 2000,
  "balance": 4000
}
```

---

## 📄 API Documentation

Swagger UI available at:
http://127.0.0.1:8000/docs

---

## 📸 Screenshots

*Add your project screenshots here (Swagger UI, API testing, etc.)*

---

## 🎯 Purpose

This project was developed to demonstrate:

* Clean Python coding practices
* REST API design
* Database integration using SQLAlchemy
* Backend architecture and business logic implementation

---

## 📌 Future Improvements

* 🔐 JWT Authentication
* 👥 Role-based access control
* 📄 Pagination
* 🔍 Advanced filtering
* ☁️ Deployment (Render / Railway)

---

## 👤 Author

**Shubham Panwar**
GitHub: https://github.com/Shubhampanwar20

---
