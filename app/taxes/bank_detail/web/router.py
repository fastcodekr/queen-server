from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse

from app.taxes.bank_detail.model.schema import BankDetailDeleteSchema, BankDetailPutSchema, BankDetailPostSchema
from app.taxes.bank_detail.web.controller import BankDetailController
from app.utils.dev.http_status_code import HttpStatusCode
from app.utils.dev.response import not_found_message

router = APIRouter()
controller = BankDetailController()


@router.get(path="", status_code=HttpStatusCode.OK.value)
async def _():
    result = not_found_message()
    return JSONResponse(content=jsonable_encoder(obj=result))


@router.post(path="", status_code=HttpStatusCode.OK.value)
async def _(vo: BankDetailPostSchema = Body(BankDetailPostSchema())):
    result = not_found_message()
    return JSONResponse(content=jsonable_encoder(obj=result))


@router.put(path="", status_code=HttpStatusCode.OK.value)
async def _(vo: BankDetailPutSchema = Body(BankDetailPutSchema())):
    result = not_found_message()
    return JSONResponse(content=jsonable_encoder(obj=result))


@router.delete(path="", status_code=HttpStatusCode.OK.value)
async def _(vo: BankDetailDeleteSchema = Body(BankDetailDeleteSchema())):
    result = not_found_message()
    return JSONResponse(content=jsonable_encoder(obj=result))
