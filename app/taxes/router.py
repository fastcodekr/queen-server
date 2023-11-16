from fastapi import APIRouter

from app.taxes.bank_detail.web.router import router as bank_detail_router

router = APIRouter()
router.include_router(bank_detail_router, prefix="/bank-detail")
