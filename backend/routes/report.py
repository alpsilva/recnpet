from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime
from .controller import db

router = APIRouter(
    prefix="/report",
    tags=['report'],
    responses={404: {"report": "Not found"}}
)

class NewReportInput(BaseModel):
    type: str
    coordinates: dict

class NewMissingReportInput(BaseModel):
    species: str
    breed: str
    fur: str
    name: str
    owner_contact: str
    owner_name: str
    last_seen_at: str
    missing_since: str
    additional_info: str

@router.get("/")
async def get_report():
    """ Returns all reports. """
    reports = db.get_all_data("reports")
    return { "reports": reports }

@router.put("/", status_code=200)
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


@router.get("/missing/")
async def get_missing_report():
    """ Returns all missing reports. """
    reports = db.get_all_data("missing_reports")
    return { "reports": reports }

@router.put("/missing/", status_code=200)
async def register_missing_report(request: NewMissingReportInput):
    """
    Receives a missing report type and coordinates from the body.
    Inserts a new rmissing eport into the databse.
    """
    
    new_report = request.dict()
    new_report["register_date"] = str(datetime.now())

    response = db.push_data("missing_reports", new_report)
    if response is None:
        raise HTTPException(status_code=500, detail="Something went wrong while inserting data.")
    return { "key": response.key }

