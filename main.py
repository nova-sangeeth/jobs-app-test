from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from server.models import Jobs


app = FastAPI()

jobs = []


@app.get("/")
def index():
    return {"hello": "There"}


@app.get("/jobs")
async def read_all():
    return jobs


@app.post("/jobs")
def create_job(job: Jobs):
    jobs.append(job.dict())
    return jobs[-1]


@app.get("/jobs/{job_id}", response_model=Jobs)
async def read_item(job_id: int):
    return jobs[job_id]


@app.delete("/jobs/{job_id}")
def delete_job(job_id: int):
    jobs.pop(job_id - 1)
    return {"message": "Removed the job"}


@app.put("/jobs/{job_id}", response_model=Jobs)
async def update_jobs(job_id: int, job: Jobs):
    update_job_encoded = jsonable_encoder(job)
    jobs[job_id] = update_job_encoded
    return update_job_encoded
