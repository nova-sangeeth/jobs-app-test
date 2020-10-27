from fastapi import FastAPI
from fastapi.requests import Request

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.routing import request_response

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/jobs/{job_id}", response_class=HTMLResponse)
async def read_item(request: Request, job_id: int):
    return templates.TemplateResponse(
        "index.html", {"request": request, "job_id": job_id}
    )
