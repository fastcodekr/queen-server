from fastapi import APIRouter

from app.customers.farm.web.router import router as farm_router
from app.customers.person.web.router import router as person_router
from app.customers.worker.web.router import router as worker_router

router = APIRouter()
router.include_router(farm_router, prefix="/farm")
router.include_router(person_router, prefix="/person")
router.include_router(worker_router, prefix="/worker")
