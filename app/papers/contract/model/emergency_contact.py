from typing import Optional

from pydantic import BaseModel


class EmergencyContactVO(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    cellPhone: Optional[str] = None
    personalDetailId: Optional[str] = None
