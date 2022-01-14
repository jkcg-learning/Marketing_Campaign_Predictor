
import pandas as pd
from pycaret.classification import load_model, predict_model
from fastapi import FastAPI
import uvicorn

# Create the app
app = FastAPI()

# Load trained Pipeline
model = load_model('final_model_api')

# Define predict function
@app.post('/predict')
def predict(id, recency, history, used_discount, used_bogo, zip_code, is_referral, channel, offer):
    data = pd.DataFrame([[id, recency, history, used_discount, used_bogo, zip_code, is_referral, channel, offer]])
    data.columns = ['id', 'recency', 'history', 'used_discount', 'used_bogo', 'zip_code', 'is_referral', 'channel', 'offer']
    predictions = predict_model(model, data=data) 
    return {'prediction': list(predictions['Label'])}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)