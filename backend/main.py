from fastapi import FastAPI
from db_connection import DbConnection

app = FastAPI()

db = DbConnection()

@app.get("/")
async def root():
    return {"message": "aaaaaaaaaaaaaaaa World"}

@app.put("/owner/")
async def register_owner():
    new_owner = {
        "name": "Pedrin Maldade Pura",
        "Catiorros": [
            {
                "name": "zezin ruim de mira"
            }
        ]
    }
    db.push_data("dono_cachorro", new_owner)
    return 200