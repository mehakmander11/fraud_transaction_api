# app/models/db_models.py

from sqlalchemy import Column, String, Float, DateTime, Boolean, Integer
from app.database.connection import Base  # Import the Base class for declarative models

class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    transaction_id = Column(String, unique=True, index=True)
    amount = Column(Float)
    timestamp = Column(DateTime)
    location = Column(String)
    device = Column(String)
    user_age = Column(Integer)
    transaction_type = Column(String)
    is_fraud = Column(Boolean)
    confidence = Column(Float)
