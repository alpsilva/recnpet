from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime
from .controller import db

router = APIRouter(
    prefix="/owner",
    tags=['owner'],
    responses={404: {"owner": "Not found"}}
)

class NewOwnerInput(BaseModel):
    name: str
    cpf: str 
    email: str
    phone: str
    address: dict

class NewPetInput(BaseModel):
    name: str
    chip: str
    race: str 
    breed: str
    stature: str

@router.put("/", status_code=200)
async def register_owner(request: NewOwnerInput):
    """ Inserts a new owner. """
    new_owner = request.dict()
    new_owner["register_date"] = str(datetime.now())

    response = db.push_data("owner", new_owner)
    if response is None:
        raise HTTPException(status_code=500, detail="Something went wrong while inserting data.")
    return { "key": response.key }

@router.get("/{cpf}/", status_code=200)
async def get_owner_by_cpf(cpf: str):
    """ Returns the owner whose cpf is the same as the given one. """
    owner = db.get_data_by_value("owner", "cpf", cpf, 1)
    if len(owner) == 0:
        raise HTTPException(status_code=404, detail="Owner not found.")
    for key, value in owner.items():
        return { "key": key, "owner": value }

@router.put("/{owner_id}/pet/", status_code=200)
async def register_pet(owner_id: str, request: NewPetInput):
    """ Inserts a new pet to owner. """

    new_pet = request.dict()
    new_pet["register_date"] = str(datetime.now())

    current_data = db.get_data_by_key("owner", owner_id, 1)
    for _, value in current_data.items():
        current_pets = value.get("pets", [])

    pets = current_pets + [new_pet]

    db.update_data_by_key(
        "owner",
        owner_id,
        { "pets": pets }
    )

    return { "pets": pets }