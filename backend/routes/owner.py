from fastapi import APIRouter, HTTPException
from datetime import datetime
from pydantic import BaseModel
from .controller import db
import time

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
    species: str 
    breed: str
    stature: str
    gender: str
    fur: str
    castrated: bool
    description: str

class NewVaccineInput(BaseModel):
    name: str
    vaccine_id: str
    applied_at: str
    valid_until: str

class NewDiseaseInput(BaseModel):
    name: str
    description: str
    symptoms: str
    spreads_by_contact: bool
    incubation_period_days: int
    veterinary_id: str
    diagonostic_date: str

@router.put("/", status_code=200)
async def register_owner(request: NewOwnerInput):
    """ Inserts a new owner. """
    new_owner = request.dict()
    new_owner["register_date"] = str(datetime.now())

    response = db.push_data("owners", new_owner)
    if response is None:
        raise HTTPException(status_code=500, detail="Something went wrong while inserting data.")
    return { "key": response.key }

@router.get("/{cpf}/", status_code=200)
async def get_owner_by_cpf(cpf: str):
    """ Returns the owner whose cpf is the same as the given one. """
    owner = db.get_data_by_value("owners", "cpf", cpf, 1)
    if len(owner) == 0:
        raise HTTPException(status_code=404, detail="Owner not found.")
    for key, value in owner.items():
        return { "key": key, "owner": value }

@router.put("/{owner_id}/pet/", status_code=200)
async def register_pet(owner_id: str, request: NewPetInput):
    """ Inserts a new pet to owner. """

    new_pet = request.dict()
    new_pet["register_date"] = str(datetime.now())
    if new_pet["chip"] == "generate":
        new_pet["chip"] = time.time_ns()

    current_data = db.get_data_by_key("owners", owner_id, 1)
    for _, value in current_data.items():
        current_pets = value.get("pets", [])

    if type(current_pets) == dict:
        current_pets = list(current_pets.values())

    pets = current_pets + [new_pet]

    db.update_data_by_key(
        "owners",
        owner_id,
        { "pets": pets }
    )

    return { "pets": pets }

@router.post("/{owner_id}/vaccine/{pet_id}/", status_code=200)
async def register_vaccine(owner_id: str, pet_id: str, request: NewVaccineInput):
    """ Inserts a vaccine register to the owner's pet. """

    new_vaccine = request.dict()
    new_vaccine["register_date"] = str(datetime.now())

    current_data = db.get_data_by_key("owners", owner_id, 1)
    for _, value in current_data.items():
        current_pets = value.get("pets", [])

    if type(current_pets) == dict:
        current_pets = list(current_pets.values())

    for pet in current_pets:
        if pet["chip"] == pet_id:
            if "vaccines" not in pet:
                pet["vaccines"] = []
            pet["vaccines"].append(new_vaccine)

    db.update_data_by_key(
        "owners",
        owner_id,
        { "pets": current_pets }
    )

    return { "pets": current_pets }

@router.post("/{owner_id}/disease/{pet_id}/", status_code=200)
async def register_disease(owner_id: str, pet_id: str, request: NewDiseaseInput):
    """ Inserts a disease register to the owner's pet. """

    new_disease = request.dict()
    new_disease["register_date"] = str(datetime.now())

    current_data = db.get_data_by_key("owners", owner_id, 1)
    for _, value in current_data.items():
        current_pets = value.get("pets", [])

    if type(current_pets) == dict:
        current_pets = list(current_pets.values())

    for pet in current_pets:
        if pet["chip"] == int(pet_id):
            if "diseases" not in pet:
                pet["diseases"] = []
            pet["diseases"].append(new_disease)

    db.update_data_by_key(
        "owners",
        owner_id,
        { "pets": current_pets }
    )

    notify_owners = set()
    incubation_time = new_disease["incubation_period_days"]
    locations = db.get_all_data("locations")

    for key, value in locations.items():
        logs = value.get("logs", [])
        for log_key, log in logs.items():
            if (datetime.today() - datetime.strptime(log["date"], "%d/%m/%Y %H:%M:%S")).days <= incubation_time:
                notify_owners.add(log["owner_id"])

    try:
        notify_owners.remove(owner_id)
    except:
        pass
        
    for other_owner in notify_owners:
        new_notification = {
            "title": "Seu animal pode ter sido exposto a uma doença.",
            "description": """
                            Um animal que frequenta uma das localizações onde você marcou presença recentemente apresentou sintomas de uma doença contagiosa.
                            Preste atenção no seu bichinho e procure ajuda profissional ao perceber qualquer sinal de comportamento anormal.
                            """,
            "register_date": str(datetime.now()),
            "owner_id": other_owner
        }
        db.push_data("notifications", new_notification)

    return { "pets": current_pets }