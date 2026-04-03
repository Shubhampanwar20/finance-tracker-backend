from sqlalchemy.orm import Session
from app import models

def create_transaction(db: Session, data, user_id):
    txn = models.Transaction(**data.dict(), user_id=user_id)
    db.add(txn)
    db.commit()
    db.refresh(txn)
    return txn

def get_transactions(db: Session):
    return db.query(models.Transaction).all()