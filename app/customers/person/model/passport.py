from typing import Optional

from pydantic import BaseModel


class PassportVO(BaseModel):
    id: Optional[str] = None
    visaGrantNumber: Optional[str] = None
    visaExpireDate: Optional[str] = None
    nationality: Optional[str] = None
    passportNumber: Optional[str] = None
    personId: Optional[str] = None
