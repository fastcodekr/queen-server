from typing import Optional

from pydantic import BaseModel

from app.papers.contract.model.emergency_contact import EmergencyContactVO
from app.papers.contract.model.superannuation import SuperannuationVO
from app.taxes.bank_detail.model.bank_detail import BankDetailVO


class PersonalDetailVO(BaseModel):
    id: Optional[str] = None
    cellPhone: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None
    taxFileNumber: Optional[str] = None
    contractId: Optional[str] = None
    emergencyContact: Optional[EmergencyContactVO] = None
    superannuation: Optional[SuperannuationVO] = None
    bankDetail: Optional[BankDetailVO] = None
