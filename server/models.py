from pydantic import BaseModel


class Jobs(BaseModel):
    job_title: str
    job_description: str
    job_specification: str
    job_salary: str
    job_qualification: str
    job_location: str


class Candidate(BaseModel):
    candidate_name: str
    candidate_address: str
    email: str
    qualification: str
