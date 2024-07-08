from fastapi import FastAPI
import joblib
from pydantic import BaseModel


app = FastAPI()


class SepsisFeatures(BaseModel):
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