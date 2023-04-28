from fastapi import APIRouter
from routes import report
from routes import owner

routes = APIRouter()

routes.include_router(report.router)
routes.include_router(owner.router)
