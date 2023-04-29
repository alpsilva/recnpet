from fastapi import APIRouter, HTTPException
from .controller import db

router = APIRouter(
    prefix="/dashboard",
    tags=['dashboard'],
    responses={404: {"dashboard": "Not found"}}
)

@router.get("/castration/", status_code=200)
async def register_owner():
    """ Returns the number of animals distributed between castrated and not, and grouped by sex. """
    response = db.get_all_data("owners")
    if response is None:
        raise HTTPException(status_code=404, detail="Something went wrong while inserting log.")
    
    pets = []
    for value in response.values(): 
            pets += value.get("pets", [])

    pets = list(filter(lambda x : x is not None, pets))

    castration = {
        "male": {
            "castrated": 0,
            "not castrated": 0
        },
        "female": {
            "castrated": 0,
            "not castrated": 0
        }
    }

    for pet in pets:
        sex = "male"
        status = "castrated"

        if pet["gender"] != "macho":
            sex = "female"

        if not pet["castrated"]:
            status = "not castrated"

        castration[sex][status] += 1

    return {
        "castration": castration
    }