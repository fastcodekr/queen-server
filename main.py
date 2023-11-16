from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware
from starlette.middleware.cors import CORSMiddleware
from starlette.templating import Jinja2Templates

from app.router import router
from app.utils.dev.config import DB_URL, QUEENSLAND_TIMEZONE
from app.utils.dev.database import init_db
from app.utils.dev.http_status_code import HttpStatusCode
from app.utils.dev.init_models import init_models
from app.utils.dev.log import LoggingMiddleware
from app.utils.dev.swagger import json_example_value
from app.utils.dev.time import current_time

templates = Jinja2Templates(directory="templates/")

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(DBSessionMiddleware, db_url=DB_URL)
app.add_middleware(LoggingMiddleware)
app.include_router(router)


@app.on_event("startup")
async def on_startup():
    await init_db()
    init_models()


@app.get(
    path="/",
    responses={
        HttpStatusCode.OK.value: json_example_value(
            data={
                "message": "Server is running",
                "timezone": QUEENSLAND_TIMEZONE,
                "current_time": current_time(),
            }
        ),
    }
)
async def root():
    return {
        "message": "Server is running",
        "timezone": QUEENSLAND_TIMEZONE,
        "current_time": current_time(),
    }
