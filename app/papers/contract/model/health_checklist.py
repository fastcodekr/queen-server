from typing import Optional

from pydantic import BaseModel

from app.papers.contract.model.general_health import GeneralHealthVO
from app.papers.contract.model.medical_condition import MedicalConditionVO
from app.papers.contract.model.mental_health import MentalHealthVO
from app.papers.contract.model.safety_aware import SafetyAwareVO


class HealthChecklistVO(BaseModel):
    id: Optional[str] = None
    extraDisclosure: Optional[str] = None
    contractId: Optional[str] = None
    generalHealth: Optional[GeneralHealthVO] = None
    mentalHealth: Optional[MentalHealthVO] = None
    safetyAware: Optional[SafetyAwareVO] = None
    medicalCondition: Optional[MedicalConditionVO] = None
