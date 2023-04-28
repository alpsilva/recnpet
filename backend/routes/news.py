from fastapi import APIRouter
from .controller import db

router = APIRouter(
    prefix="/news",
    tags=['news'],
    responses={404: {"news": "Not found"}}
)

@router.get("/", status_code=200)
async def get_active_news():
    """ Returns the news whose "active" field is true. """
    result = db.get_data_by_value("news", "active", True)
    news = []
    for _, value in result.items():
        news.append(value)
    
    return { "news": news }