from fastapi import FastAPI
import joblib
import pandas as pd
from pydantic import BaseModel
import os

# Get the absolute path of the current script (api.py)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the correct path to the model file
model_path = os.path.join(current_dir, "../models/fraud_detection_model.pkl")

# Load the model
model = joblib.load(model_path)

# Step 2: Initialize FastAPI app
app = FastAPI()

# Step 3: Define the input data format
class Transaction(BaseModel):
    V17: float
    V14: float
    V12: float
    V10: float
    V11: float
    V16: float
    V4: float
    V3: float
    V18: float
    V9: float
    Amount: float
    Time: float

# Step 4: Create the prediction endpoint
@app.post("/predict")
def predict_fraud(transaction: Transaction):
    # Convert input data to DataFrame
    input_data = pd.DataFrame([transaction.dict()])

    # Make prediction
    prediction = model.predict(input_data)

    # Return fraud status
    return {"fraud_prediction": int(prediction[0])}