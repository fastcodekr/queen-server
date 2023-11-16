from typing import Optional

from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse

from app.customers.worker.model.schema import WorkerDeleteSchema, WorkerPutSchema, WorkerPostSchema
from app.customers.worker.web.controller import WorkerController
from app.utils.dev.http_status_code import HttpStatusCode
from app.utils.dev.response import not_found_message

router = APIRouter()
controller = WorkerController()


@router.get(path="", status_code=HttpStatusCode.OK.value)
async def _(by: Optional[str] = None,
            id: Optional[int] = None):
    if by == "all":
        result = controller.customers_worker_by_all()
    elif id:
        result = controller.customers_worker_id()
    else:
        result = not_found_message()
    return JSONResponse(content=jsonable_encoder(obj=result))


@router.post(path="", status_code=HttpStatusCode.OK.value)
async def _(vo: WorkerPostSchema = Body(WorkerPostSchema())):
    result = not_found_message()
    return JSONResponse(content=jsonable_encoder(obj=result))


@router.put(path="", status_code=HttpStatusCode.OK.value)
async def _(vo: WorkerPutSchema = Body(WorkerPutSchema())):
    result = not_found_message()
    return JSONResponse(content=jsonable_encoder(obj=result))


@router.delete(path="", status_code=HttpStatusCode.OK.value)
async def _(vo: WorkerDeleteSchema = Body(WorkerDeleteSchema())):
    result = not_found_message()
    return JSONResponse(content=jsonable_encoder(obj=result))
