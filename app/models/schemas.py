from pydantic import BaseModel
from datetime import datetime

class PredictionRequest(BaseModel):
    transaction_id: str
    amount: float
    location: str
    device:str
    user_age: int
    transaction_type: str
    timestamp: datetime

class PredictionResponse(BaseModel):
    transaction_id: str
    is_fraud: bool
    confidence: float # Confidence score of the prediction and optional

    class config:
        orm_mode = True