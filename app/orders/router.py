from fastapi import APIRouter

from app.orders.order.web.router import router as order_router
from app.orders.pay.web.router import router as pay_router

router = APIRouter()
router.include_router(order_router, prefix="/order")
router.include_router(pay_router, prefix="/pay")
