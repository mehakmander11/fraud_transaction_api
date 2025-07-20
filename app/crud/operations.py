from sqlalchemy.orm import Session  # orm is used to interact with the database and python objects
from app.models.schemas import PredictionRequest, PredictionResponse
from app.models.db_models import Prediction

def save_prediction(db: Session, input_data: PredictionRequest, is_fraud: bool, confidence: float):
    
    # save a prediction to the database and return the response.
    
    # Create a new prediction object
    prediction = Prediction(
        transaction_id=input_data.transaction_id,
        amount=input_data.amount,
        location=input_data.location,
        device=input_data.device,
        user_age=input_data.user_age,
        transaction_type=input_data.transaction_type,
        timestamp=input_data.timestamp,
        
        is_fraud=is_fraud,
        confidence=confidence
    )
    
    # Add the prediction to the session
    db.add(prediction)
    db.commit()
    db.refresh(prediction)  # Refresh to get the updated object 

    # Return the response
    return prediction