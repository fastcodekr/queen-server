from typing import Optional

from pydantic import BaseModel


class MedicalConditionVO(BaseModel):
    id: Optional[str] = None
    beeSting: Optional[str] = None
    epilepsy: Optional[str] = None
    diabetes: Optional[str] = None
    pregnant: Optional[str] = None
    highBloodPressure: Optional[str] = None
    other: Optional[str] = None
    healthChecklistId: Optional[str] = None
