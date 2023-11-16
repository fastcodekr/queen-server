from fastapi import APIRouter

from app.utils.draft53.web.router import router as draft53_router

router = APIRouter()
router.include_router(draft53_router, prefix="/draft53")
