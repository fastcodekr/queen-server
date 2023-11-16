from fastapi import APIRouter

from app.systems.company.web.router import router as company_router
from app.systems.staff.web.router import router as staff_router

router = APIRouter()
router.include_router(company_router, prefix="/company")
router.include_router(staff_router, prefix="/staff")
