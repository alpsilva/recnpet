from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime
from controller import db

router = APIRouter(
    prefix="/report",
    tags=['report'],
    responses={404: {"report": "Not found"}}
)

class NewReportInput(BaseModel):
    type: str
    coordinates: dict

@router.get("/report/")
async def get_report():
    """ Returns all reports. """
    reports = db.get_all_data("reports")
    return { "reports": reports }

@router.put("/report/", status_code=200)
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

