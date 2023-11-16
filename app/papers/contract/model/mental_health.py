from typing import Optional

from pydantic import BaseModel


class MentalHealthVO(BaseModel):
    id: Optional[str] = None
    jobStress: Optional[str] = None
    mentalCounseling: Optional[str] = None
    awareOfEap: Optional[str] = None
    healthChecklistId: Optional[str] = None
