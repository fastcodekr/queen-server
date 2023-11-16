from fastapi import APIRouter

from app.authors.author.web.router import router as author_router
from app.authors.finder.web.router import router as finder_router
from app.authors.valid.web.router import router as valid_router

router = APIRouter()
router.include_router(author_router, prefix="/author")
router.include_router(finder_router, prefix="/finder")
router.include_router(valid_router, prefix="/valid")
