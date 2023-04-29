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
        raise HTTPException(status_code=404, detail="Something went wrong while retrieving data.")
    
    pets = []
    for value in response.values():
            address = value.get("address", {})
            for pet in value.get("pets", []):
                 if pet is not None:
                      pet["address"] = address
                      pets.append(pet)

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

    locations = {}

    for pet in pets:
        location = pet["address"]["neighborhood"]
        if location not in locations:
             locations[location] = {
                  "pets": 0,
                  "diseases": {},
                  "totalDiseases": 0
             }

        locations[location]["pets"] += 1
        
        pet_diseases = pet.get("diseases", [])
        for disease in pet_diseases:
            locations[location]["totalDiseases"] += 1
            disease_name = disease["name"]
            if disease_name not in locations[location]["diseases"]:
                locations[location]["diseases"][disease_name] = 0
            locations[location]["diseases"][disease_name] += 1

        sex = "male"
        status = "castrated"

        if pet["gender"] != "macho":
            sex = "female"

        if not pet["castrated"]:
            status = "not castrated"

        castration[sex][status] += 1

    return {
        "castration": castration,
        "locations": locations
    }