from typing import Optional

from pydantic import BaseModel


class SafetyAwareVO(BaseModel):
    id: Optional[str] = None
    awareOfSafetyPolicy: Optional[str] = None
    firstAidTraining: Optional[str] = None
    safetyReportingComfort: Optional[str] = None
    healthChecklistId: Optional[str] = None
