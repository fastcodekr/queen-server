from fastapi import APIRouter

from app.quotes.calculator.web.router import router as calculator_router

router = APIRouter()
router.include_router(calculator_router, prefix="/calculator")
