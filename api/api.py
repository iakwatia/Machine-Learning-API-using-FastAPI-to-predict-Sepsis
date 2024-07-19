from fastapi import FastAPI
import joblib
from pydantic import BaseModel
import pandas as pd


app = FastAPI()


class SepssisFeatures(BaseModel):
    PRG : int       
    PL : int        
    PR : int        
    SK : int        
    TS : int       
    M11 : float        
    BD2 : float       
    Age : int      
    Insurance : int  
           
         
         
@app.get('/')
def status_check():
    return{"Status": "API is live..."}


GradientBoost_pipeline = joblib.load('./models/GradientBoost_pipeline.joblib')
forest_pipeline = joblib.load('./models/forest_pipeline.joblib')
encoder = joblib.load('./models/encoder.joblib')


@app.post("/forest_prediction")
def predict_sepsis(data: SepssisFeatures):

    df = pd.DataFrame([data.model_dump()])

    
    prediction = forest_pipeline.predict(df)
    probability = forest_pipeline.predict_proba(df)

    prediction = int(prediction[0])

    prediction = encoder.inverse_transform([prediction])[0]

    if prediction == 'Negative':
            probability= f'{round(probability[0][0], 2)*100}%'
    else:
            probability = f'{round(probability[1][0], 2)*100}%'

    return {"prediction": prediction, "probability": probability}



@app.post("/gradientboost_prediction")
def predict_sepsis(data: SepssisFeatures):

    df = pd.DataFrame([data.model_dump()])

    
    prediction = GradientBoost_pipeline.predict(df)
    probability = GradientBoost_pipeline.predict_proba(df)


    prediction = int(prediction[0])

    prediction = encoder.inverse_transform([prediction])[0]

    if prediction == 'Negative':
            probability= f'{round(probability[0][0], 2)*100}%'
    else:
            probability = f'{round(probability[0][1], 2)*100}%'

    return {"prediction": prediction, "probability": probability}


   
