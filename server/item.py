from os import name
from fastapi import FastAPI

# from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from tortoise import fields
from tortoise.fields.relational import ForeignKeyField
from tortoise.models import Model
from tortoise.contrib.fastapi import register_tortoise
from tortoise.contrib.pydantic import pydantic_model_creator
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()


class Jobs(Model):
    id = fields.IntField(pk=True)
    job_title = fields.CharField(128, null=True)
    job_description = fields.CharField(128, null=True)
    job_requirements = fields.CharField(128, null=True)
    job_location = fields.CharField(128, null=True)
    job_timings = fields.CharField(128, null=True)
    job_salary = fields.IntField(null=True)
    applied = fields.BooleanField(default=False, null=True)

class jobapplication(Model):
    id = fields.IntField(pk=True)
    job_id = fields.ForeignKeyField('models.Jobs', related_name='jobapplication', on_delete='CASCADE', db_constraint=True, null= True)
    comments = fields.CharField(256, null=True)
    
class companies_available(Model):
    id = fields.IntField(pk=True)
    company_name = fields.CharField(256, null=True)
    company_location = fields.CharField(128, null=True)


Jobs_Pydantic = pydantic_model_creator(Jobs, name="Jobs")
JobsIn_Pydantic = pydantic_model_creator(Jobs, name="JobsIn", exclude_readonly=True)

# pydantic generation for companies available;
companies_available_Pydantic = pydantic_model_creator(
    companies_available, name="companies_available"
)
companies_available_InPydantic = pydantic_model_creator(
    companies_available, name="companies_availableIn", exclude_readonly=True
)
job_application_pydantic = pydantic_model_creator(jobapplication, name= "job_application")
jobIn_application_pydantic = pydantic_model_creator(jobapplication, name= "jobIn_application", exclude_readonly=True)

origins = [
    "http://172.17.72.240:8080/",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8081",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/jobs/add")
async def create_job(job: JobsIn_Pydantic):
    job_obj = await Jobs.create(**job.dict(exclude_unset=True, exclude={"id"}))
    return await Jobs_Pydantic.from_tortoise_orm(job_obj)


# show all the jobs.
@app.get("/jobs")
async def get_all_jobs():
    return await Jobs_Pydantic.from_queryset(Jobs.all())


# blank field
@app.get("/")
async def index():
    return {"Hello There, Welcome to the jobs api."}


# show by id
@app.get("/jobs/{job_id}")
async def get_job_by_id(job_id: int):
    return await Jobs_Pydantic.from_queryset_single(Jobs.get(id=job_id))


# apply by id
@app.get("/jobs/{job_id}/apply")
async def get_job_by_id(job_id: int):

    return {"Thanks for applying, We will get back to you as soon as possible."}


# delete_by_id
@app.delete("/jobs/delete/{job_id}")
async def delete_job(job_id: int):
    await Jobs.filter(id=job_id).delete()
    return {"deleted": "object"}


# update_by_id
@app.put("/jobs/update/{job_id}", response_model=Jobs_Pydantic)
async def update_job(job_id: int, job: JobsIn_Pydantic):
    await Jobs.filter(id=job_id).update(**job.dict(exclude_unset=True, exclude={"id"}))
    return await Jobs_Pydantic.from_queryset_single(Jobs.get(id=job_id))


# endpoints for companies available.:
@app.post("/companies/add")
async def add_companies(company: companies_available_InPydantic):
    company_obj = await companies_available.create(
        **company.dict(exclude_unset=True, exclude={"id"})
    )
    return await companies_available_InPydantic.from_tortoise_orm(company_obj)


@app.get("/companies/all")
async def get_all_companies():
    return await companies_available_Pydantic.from_queryset(companies_available.all())


@app.get("/companies/{company_id}/")
async def get_companies_by_id(company_id: int):
    return await companies_available_Pydantic.from_queryset_single(
        companies_available.get(id=company_id)
    )


# update needs a response to add a response model always for tortoise orm.
@app.put("/company/update/{company_id}/", response_model=companies_available_Pydantic)
async def update_company_by_id(
    company_id: int, company: companies_available_InPydantic
):
    await companies_available.filter(id=company_id).update(
        **company.dict(exclude_unset=True, exclude={"id"})
    )
    return await companies_available_Pydantic.from_queryset_single(
        companies_available.get(id=company_id)
    )


@app.delete("/company/delete/{company_id}/")
async def delete_company(company_id: int):
    await companies_available.filter(id=company_id).delete()
    return {"company": "deleted"}

@app.post('/jobs/apply/{job_id}', response_model=job_application_pydantic)
async def apply_job(job_apply: jobIn_application_pydantic, job_id: int):
    job_application_obj = await jobapplication.create(
        **job_apply.dict(exclude_unset=True, exclude={"id"})
    )
    return await jobIn_application_pydantic.from_tortoise_orm(job_application_obj)

    



register_tortoise(
    app,
    db_url="sqlite://db.sqlite3",
    modules={"models": ["item"]},
    generate_schemas=True,
    add_exception_handlers=True,
)