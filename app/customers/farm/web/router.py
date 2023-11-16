from typing import Optional

from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse

from app.customers.farm.model.schema import FarmPostSchema, FarmPutSchema, FarmDeleteSchema
from app.customers.farm.web.controller import FarmController
from app.utils.dev.http_status_code import HttpStatusCode
from app.utils.dev.response import not_found_message

router = APIRouter()
controller = FarmController()


@router.get(path="", status_code=HttpStatusCode.OK.value)
async def _(by: Optional[str] = None):
    if by == "location":
        result = controller.customers_farm_by_location()
    else:
        result = not_found_message()
    return JSONResponse(content=jsonable_encoder(obj=result))


@router.post(path="", status_code=HttpStatusCode.OK.value)
async def _(vo: FarmPostSchema = Body(FarmPostSchema())):
    result = not_found_message()
    return JSONResponse(content=jsonable_encoder(obj=result))


@router.put(path="", status_code=HttpStatusCode.OK.value)
async def _(vo: FarmPutSchema = Body(FarmPutSchema())):
    result = not_found_message()
    return JSONResponse(content=jsonable_encoder(obj=result))


@router.delete(path="", status_code=HttpStatusCode.OK.value)
async def _(vo: FarmDeleteSchema = Body(FarmDeleteSchema())):
    result = not_found_message()
    return JSONResponse(content=jsonable_encoder(obj=result))
