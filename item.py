from os import name
from fastapi import FastAPI

# from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from tortoise import fields
from tortoise.models import Model
from tortoise.contrib.fastapi import register_tortoise
from tortoise.contrib.pydantic import pydantic_model_creator

app = FastAPI()


class Jobs(Model):
    # id = fields.IntField(pk=True)
    job_title = fields.CharField(128)
    job_Description = fields.CharField(128)
    job_requirements = fields.CharField(128)
    job_location = fields.CharField(128)
    job_timings = fields.CharField(128)
    job_salary = fields.IntField()


Jobs_Pydantic = pydantic_model_creator(Jobs, name="Jobs")
JobsIn_Pydantic = pydantic_model_creator(Jobs, name="Jobs", exclude_readonly=True)


origins = [
    "http://172.17.72.240:8080/",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/jobs/add")
async def create_job(job: JobsIn_Pydantic):
    job_obj = await Jobs.create(**job.dict(exclude_unset=True))
    return await Jobs_Pydantic.from_tortoise_orm(job_obj)


# show all the jobs.
@app.get("/jobs")
async def get_all_jobs():
    return await Jobs_Pydantic.from_queryset(Jobs.all())


# show by id
@app.get("/jobs/{job_id}")
async def get_job_by_id(job_id: int):
    return await Jobs_Pydantic.from_queryset_single(Jobs.get(id=job_id))


# delete_by_id
@app.delete("/jobs/{job_id}")
async def delete_job(job_id: int):
    await Jobs.filter(id=job_id).delete()
    return {"deleted": "object"}


# @app.put("/items/edit/{item_id}", response_model=Items)
# async def update_item(item_id: int, item: Items):
#     update_item_encoded = jsonable_encoder(item)
#     items[item_id] = update_item_encoded
#     return update_item_encoded


register_tortoise(
    app,
    db_url="sqlite://db.sqlite3",
    modules={"models": ["item"]},
    generate_schemas=True,
    add_exception_handlers=True,
)