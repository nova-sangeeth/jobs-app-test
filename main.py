from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from server.models import Jobs


app = FastAPI()

jobs = []


@app.get("/")
def index():
    return {"hello": "There"}
