from typing import Optional

from pydantic import BaseModel


class GeneralHealthVO(BaseModel):
    id: Optional[str] = None
    preExistingMedicalCondition: Optional[str] = None
    takingMedication: Optional[str] = None
    recentSurgery: Optional[str] = None
    recentInjury: Optional[str] = None
    jobRelatedLimitation: Optional[str] = None
    healthChecklistId: Optional[str] = None
