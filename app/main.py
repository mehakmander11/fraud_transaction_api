#psycopg2- postgresql driver
from fastapi import FastAPI, Depends    
from app.database.connection import get_db
from sqlalchemy.orm import Session
from app.api.routes import router

app = FastAPI()

@app.get("/")
def root(db: Session = Depends(get_db)):
    return {"message": "Fraud Detection API is running!"}

# Include the API router
app.include_router(router, prefix="/api", tags=["fraud_detection"])
