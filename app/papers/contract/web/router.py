from typing import Optional

from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse

from app.papers.contract.model.schema import ContractDeleteSchema, ContractPutSchema, ContractPostSchema
from app.papers.contract.web.controller import ContractController
from app.utils.dev.http_status_code import HttpStatusCode
from app.utils.dev.response import not_found_message

router = APIRouter()
controller = ContractController()


@router.get(path="", status_code=HttpStatusCode.OK.value)
async def _():
    result = not_found_message()
    return JSONResponse(content=jsonable_encoder(obj=result))


@router.post(path="", status_code=HttpStatusCode.OK.value)
async def _(do: Optional[str] = None,
            vo: ContractPostSchema = Body(ContractPostSchema()), ):
    if do == "add":
        result = controller.papers_contract_do_add(vo=vo)
    else:
        result = not_found_message()
    return JSONResponse(content=jsonable_encoder(obj=result))


@router.put(path="", status_code=HttpStatusCode.OK.value)
async def _(vo: ContractPutSchema = Body(ContractPutSchema())):
    result = not_found_message()
    return JSONResponse(content=jsonable_encoder(obj=result))


@router.delete(path="", status_code=HttpStatusCode.OK.value)
async def _(vo: ContractDeleteSchema = Body(ContractDeleteSchema()), ):
    result = not_found_message()
    return JSONResponse(content=jsonable_encoder(obj=result))
