from routes.api import routes
from fastapi import FastAPI

app = FastAPI()

app.include_router(routes)
    