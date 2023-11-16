from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse

from app.utils.dev.http_status_code import HttpStatusCode
from app.utils.dev.response import not_found_message
from app.utils.draft53.model.schema import Draft53DeleteSchema, Draft53PutSchema, Draft53PostSchema
from app.utils.draft53.web.controller import Draft53Controller

router = APIRouter()
controller = Draft53Controller()


@router.get(path="", status_code=HttpStatusCode.OK.value)
async def _():
    result = not_found_message()
    return JSONResponse(content=jsonable_encoder(obj=result))


@router.post(path="", status_code=HttpStatusCode.OK.value)
async def _(vo: Draft53PostSchema = Body(Draft53PostSchema())):
    result = not_found_message()
    return JSONResponse(content=jsonable_encoder(obj=result))


@router.put(path="", status_code=HttpStatusCode.OK.value)
async def _(vo: Draft53PutSchema = Body(Draft53PutSchema())):
    result = not_found_message()
    return JSONResponse(content=jsonable_encoder(obj=result))


@router.delete(path="", status_code=HttpStatusCode.OK.value)
async def _(vo: Draft53DeleteSchema = Body(Draft53DeleteSchema())):
    result = not_found_message()
    return JSONResponse(content=jsonable_encoder(obj=result))
