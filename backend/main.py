from fastapi import FastAPI, HTTPException
from db_connection import DbConnection
from datetime import datetime
from pydantic import BaseModel

app = FastAPI()

db = DbConnection()

@app.get("/")
async def root():
    return {"message": "aaaaaaaaaaaaaaaa World"}

@app.put("/owner/")
async def register_owner():
    new_owner = {
        "name": "Pedrin Maldade Pura",
        "Catiorros": [
            {
                "name": "zezin ruim de mira"
            }
        ]
    }
    db.push_data("dono_cachorro", new_owner)
    return 200

class NewReportInput(BaseModel):
    type: str
    coordinates: dict
    
@app.put("/report/", status_code=200)
async def register_report(request: NewReportInput):
    """
    Receives a report type and coordinates from the body.
    Inserts a new report into the databse.
    """
    
    new_report = {
        "type": request.type,
        "coordinates": request.coordinates,
        "date": str(datetime.now())
    }
    response = db.push_data("reports", new_report)
    if response is None:
        raise HTTPException(status_code=500, detail="Something went wrong while inserting data.")
    return { "key": response.key }
    