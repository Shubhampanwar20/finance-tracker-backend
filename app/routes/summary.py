from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models
from sqlalchemy import func

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/summary")
def get_summary(db: Session = Depends(get_db)):
    income = db.query(func.sum(models.Transaction.amount)).filter(
        models.Transaction.type == "income"
    ).scalar() or 0

    expense = db.query(func.sum(models.Transaction.amount)).filter(
        models.Transaction.type == "expense"
    ).scalar() or 0

    return {
        "total_income": income,
        "total_expense": expense,
        "balance": income - expense
    }