import joblib
import pandas as pd
import os

# Load the model
model_path = os.path.join(os.path.dirname(__file__), "pipeline.joblib")
model = joblib.load(model_path)

def make_prediction(input_data: dict):
    df = pd.DataFrame([input_data])
    prediction = model.predict(df)[0]
    confidence = max(model.predict_proba(df)[0])
    
    return bool(prediction), float(round(confidence, 2)) 
# Ensure the prediction is boolean and confidence is float
# This ensures that the response is compatible with the Pydantic model
