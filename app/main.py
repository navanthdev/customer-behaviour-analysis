from fastapi import FastAPI
from sqlalchemy import create_engine
app=FastAPI()
DATABASE_URL='mysql+pymysql://root:navanth@localhost:3306/customer_behaviour_analysis'
engine=create_engine(DATABASE_URL)
@app.get('/test')
def get_connection():
  with engine.connect() as connection:
    if connection:
      return {
          'message':'connection established'
      }
    return{
        'message':'connection failed'
    }


