from fastapi import APIRouter

from app.authors.router import router as authors_router
from app.boards.router import router as boards_router
from app.customers.router import router as customers_router
from app.orders.router import router as orders_router
from app.papers.router import router as papers_router
from app.quotes.router import router as quotes_router
from app.systems.router import router as systems_router
from app.taxes.router import router as taxes_router
from app.utils.router import router as utils_router

router = APIRouter()
router.include_router(authors_router, prefix="/authors")
router.include_router(boards_router, prefix="/boards")
router.include_router(customers_router, prefix="/customers")
router.include_router(orders_router, prefix="/orders")
router.include_router(papers_router, prefix="/papers")
router.include_router(quotes_router, prefix="/quotes")
router.include_router(systems_router, prefix="/systems")
router.include_router(taxes_router, prefix="/taxes")
router.include_router(utils_router, prefix="/utils")
