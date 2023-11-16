from typing import Optional

from pydantic import BaseModel

from app.systems.company.model.company import CompanyVO
from app.systems.team.model.team import TeamVO


class StaffVO(BaseModel):
    id: Optional[str] = None
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None
    level: Optional[str] = None
    name: Optional[str] = None
    password: Optional[str] = None
    companyArray: Optional[list[CompanyVO]] = None
    teamArray: Optional[list[TeamVO]] = None
