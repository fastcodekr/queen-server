from fastapi import APIRouter

from app.papers.contract.web.router import router as contract_router
from app.papers.contract_form.web.router import router as contract_form_router

router = APIRouter()
router.include_router(contract_router, prefix="/contract")
router.include_router(contract_form_router, prefix="/contract-form")
