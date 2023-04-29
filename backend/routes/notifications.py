from fastapi import APIRouter, HTTPException
from .controller import db

router = APIRouter(
    prefix="/notifications",
    tags=['notifications'],
    responses={404: {"notifications": "Not found"}}
)

@router.get("/{owner_id}/", status_code=200)
async def get_all_user_notifications(owner_id):
    """ Returns all the notifications of the given user. """
    response = db.get_data_by_value("notifications", "owner_id", owner_id)
    if response is None:
        raise HTTPException(status_code=404, detail="Something went wrong while retrieving data.")
    
    notifications = []
    for _, value in response.items():
        notifications.append(value)

    return { "notifications": notifications }
    
    