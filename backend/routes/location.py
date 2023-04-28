from fastapi import APIRouter, HTTPException
from datetime import datetime, timedelta
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
        "date": datetime.strftime(datetime.now(), "%d/%m/%Y %H:%M:%S")
    }

    response = db.add_to_array_data_by_key("locations", location_id, new_log)
    if response is None:
        raise HTTPException(status_code=500, detail="Something went wrong while inserting log.")

    return { "key": response.key }

@router.get("/{location_id}/pets/", status_code=200)
async def get_animals_in_location(location_id: str):
    """ Returns a list of pets that checked in at the location in the last hours.  """
    end = datetime.now()
    start = end - timedelta(hours=2)

    def in_timeframe(log_time: str):
        log_time = datetime.strptime(log_time, "%d/%m/%Y %H:%M:%S") 
        return log_time >= start

    result = db.get_data_by_key("locations", location_id)
    for key, value in result.items():
        logs = value.get("logs")
        location_name = value.get("name")

    owners = set()
    for key, value in logs.items():
        if in_timeframe(value["date"]):
            owners.add(value["owner_id"])

    pets = []
    for owner_id in owners:
        result = db.get_data_by_key("owners", owner_id)
        if result is not None:
            for key, value in result.items():
                owner_pets = value.get("pets", [])
                for pet in owner_pets:
                    pets.append({
                        "pet": pet,
                        "owner": owner_id
                    })

    return {"pets": pets}