from fastapi import APIRouter
from routes import report

routes = APIRouter()

routes.include_router(report.router)