from typing import Optional

from pydantic import BaseModel

from app.boards.board.model.board import BoardVO
from app.customers.farm.model.farm import FarmVO
from app.systems.team.model.team import TeamVO


class CompanyVO(BaseModel):
    id: Optional[str] = None
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None
    name: Optional[str] = None
    address: Optional[str] = None
    staffId: Optional[str] = None
    boardArray: Optional[list[BoardVO]] = None
    farmArray: Optional[list[FarmVO]] = None
    teamArray: Optional[list[TeamVO]] = None
