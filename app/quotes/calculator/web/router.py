from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse

from app.quotes.calculator.model.schema import CalculatorDeleteSchema, CalculatorPutSchema, CalculatorPostSchema
from app.quotes.calculator.web.controller import CalculatorController
from app.utils.dev.http_status_code import HttpStatusCode
from app.utils.dev.response import not_found_message

router = APIRouter()
controller = CalculatorController()


@router.get(path="", status_code=HttpStatusCode.OK.value)
async def _():
    result = not_found_message()
    return JSONResponse(content=jsonable_encoder(obj=result))


@router.post(path="", status_code=HttpStatusCode.OK.value)
async def _(vo: CalculatorPostSchema = Body(CalculatorPostSchema())):
    result = not_found_message()
    return JSONResponse(content=jsonable_encoder(obj=result))


@router.put(path="", status_code=HttpStatusCode.OK.value)
async def _(vo: CalculatorPutSchema = Body(CalculatorPutSchema())):
    result = not_found_message()
    return JSONResponse(content=jsonable_encoder(obj=result))


@router.delete(path="", status_code=HttpStatusCode.OK.value)
async def _(vo: CalculatorDeleteSchema = Body(CalculatorDeleteSchema())):
    result = not_found_message()
    return JSONResponse(content=jsonable_encoder(obj=result))
