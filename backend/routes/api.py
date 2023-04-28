from fastapi import APIRouter
from routes import location
from routes import report
from routes import owner
from routes import news

routes = APIRouter()

routes.include_router(location.router)
routes.include_router(report.router)
routes.include_router(owner.router)
routes.include_router(news.router)
