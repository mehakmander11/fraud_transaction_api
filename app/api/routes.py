from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.models.schemas import PredictionRequest, PredictionResponse
from app.crud.operations import save_prediction
from app.ml.predict import make_prediction  # import your prediction function


router = APIRouter()
@router.post("/predict", response_model=PredictionResponse)
def predict_fraud(request: PredictionRequest, db: Session = Depends(get_db)):
    # Make the prediction using the ML model
    try:
        is_fraud, confidence = make_prediction(request.dict())
        # Save the prediction to the database
        save_prediction(db, request, is_fraud, confidence)
        return PredictionResponse(
            transaction_id=request.transaction_id,
            is_fraud=is_fraud,
            confidence=confidence
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))