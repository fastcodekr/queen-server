from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse

from app.authors.finder.model.schema import FinderPostSchema, FinderPutSchema, FinderDeleteSchema
from app.authors.finder.web.controller import FinderController
from app.utils.dev.http_status_code import HttpStatusCode
from app.utils.dev.response import not_found_message

router = APIRouter()
controller = FinderController()


@router.get(path="", status_code=HttpStatusCode.OK.value)
async def _():
    result = not_found_message()
    return JSONResponse(content=jsonable_encoder(obj=result))


@router.post(path="", status_code=HttpStatusCode.OK.value)
async def _(vo: FinderPostSchema = Body(FinderPostSchema())):
    result = not_found_message()
    return JSONResponse(content=jsonable_encoder(obj=result))


@router.put(path="", status_code=HttpStatusCode.OK.value)
async def _(vo: FinderPutSchema = Body(FinderPutSchema())):
    result = not_found_message()
    return JSONResponse(content=jsonable_encoder(obj=result))


@router.delete(path="", status_code=HttpStatusCode.OK.value)
async def _(vo: FinderDeleteSchema = Body(FinderDeleteSchema())):
    result = not_found_message()
    return JSONResponse(content=jsonable_encoder(obj=result))
