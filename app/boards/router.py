from fastapi import APIRouter

from app.boards.board.web.router import router as board_router

router = APIRouter()
router.include_router(board_router, prefix="/board")
