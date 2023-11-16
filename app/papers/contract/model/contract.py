from typing import Optional

from pydantic import BaseModel

from app.papers.contract.model.health_checklist import HealthChecklistVO
from app.papers.contract.model.personal_detail import PersonalDetailVO


class ContractVO(BaseModel):
    id: Optional[str] = None
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None
    workerId: Optional[str] = None
    personalDetail: Optional[PersonalDetailVO] = None
    healthChecklist: Optional[HealthChecklistVO] = None
