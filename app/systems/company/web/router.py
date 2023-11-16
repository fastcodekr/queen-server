from typing import Optional

from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse

from app.systems.company.model.schema import CompanyDeleteSchema, CompanyPutSchema, CompanyPostSchema
from app.systems.company.web.controller import CompanyController
from app.utils.dev.http_status_code import HttpStatusCode
from app.utils.dev.response import not_found_message

router = APIRouter()
controller = CompanyController()


@router.get(path="", status_code=HttpStatusCode.OK.value)
async def _(by: Optional[str] = None):
    if by == "all":
        result = controller.systems_company_by_all()
    elif by != "all" and by:
        result = controller.systems_company_by_name(by=by)
    else:
        result = not_found_message()
    return JSONResponse(content=jsonable_encoder(obj=result))


@router.post(path="", status_code=HttpStatusCode.OK.value)
async def _(vo: CompanyPostSchema = Body(CompanyPostSchema())):
    result = not_found_message()
    return JSONResponse(content=jsonable_encoder(obj=result))


@router.put(path="", status_code=HttpStatusCode.OK.value)
async def _(vo: CompanyPutSchema = Body(CompanyPutSchema())):
    result = not_found_message()
    return JSONResponse(content=jsonable_encoder(obj=result))


@router.delete(path="", status_code=HttpStatusCode.OK.value)
async def _(vo: CompanyDeleteSchema = Body(CompanyDeleteSchema())):
    result = not_found_message()
    return JSONResponse(content=jsonable_encoder(obj=result))
