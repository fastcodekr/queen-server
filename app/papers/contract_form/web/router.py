from typing import Optional

from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse

from app.papers.contract_form.model.schema import ContractFormPostSchema, ContractFormPutSchema, \
    ContractFormDeleteSchema
from app.papers.contract_form.web.controller import ContractFormController
from app.utils.dev.http_status_code import HttpStatusCode
from app.utils.dev.response import not_found_message

router = APIRouter()
controller = ContractFormController()


@router.get(path="", status_code=HttpStatusCode.OK.value)
async def _(by: Optional[str] = None):
    strategy = {
        "policy": controller.papers_contract_form_by_policy(),
        "agree": controller.papers_contract_form_by_agree(),
        "schedule": controller.papers_contract_form_by_schedule(),
        "guideline": controller.papers_contract_form_by_guideline(),
        "checklist": controller.papers_contract_form_by_checklist(),
    }
    if by in strategy.keys():
        result = strategy.get(by)
    else:
        result = not_found_message()
    return JSONResponse(content=jsonable_encoder(obj=result))


@router.post(path="", status_code=HttpStatusCode.OK.value)
async def _(vo: ContractFormPostSchema = Body(ContractFormPostSchema())):
    result = not_found_message()
    return JSONResponse(content=jsonable_encoder(obj=result))


@router.put(path="", status_code=HttpStatusCode.OK.value)
async def _(vo: ContractFormPutSchema = Body(ContractFormPutSchema())):
    result = not_found_message()
    return JSONResponse(content=jsonable_encoder(obj=result))


@router.delete(path="", status_code=HttpStatusCode.OK.value)
async def _(vo: ContractFormDeleteSchema = Body(ContractFormDeleteSchema())):
    result = not_found_message()
    return JSONResponse(content=jsonable_encoder(obj=result))
