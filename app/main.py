from fastapi import FastAPI
from app.database import Base, engine
from app.routes import transaction, summary

app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(transaction.router)
app.include_router(summary.router)

@app.get("/")
def home():
    return {"message": "Finance Tracker API Running 🚀"}