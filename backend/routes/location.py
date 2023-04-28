from fastapi import APIRouter, HTTPException
from datetime import date
from .controller import db

router = APIRouter(
    prefix="/location",
    tags=['location'],
    responses={404: {"location": "Not found"}}
)

@router.post("/{location_id}/register/{owner_id}/", status_code=200)
async def register_owner(location_id: str, owner_id: str):
    """ Register the owner_id in the log of the location. """
    new_log = {
        "owner_id": owner_id,
        "date": str(date.today())
    }

    response = db.add_to_array_data_by_key("locations", location_id, new_log)
    if response is None:
        raise HTTPException(status_code=500, detail="Something went wrong while inserting log.")

    return {}
