from typing import Optional

from pydantic import BaseModel

from app.orders.order.model.order import OrderVO
from app.papers.contract.model.contract import ContractVO


class WorkerVO(BaseModel):
    id: Optional[str] = None
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None
    startDate: Optional[str] = None
    endDate: Optional[str] = None
    tax: Optional[str] = None
    farmNumber: Optional[str] = None
    memo: Optional[str] = None
    teamId: Optional[str] = None
    personId: Optional[str] = None
    contract: Optional[ContractVO] = None
    orderArray: Optional[list[OrderVO]] = None


class WorkerViewTableVO(BaseModel):
    id: Optional[str] = None
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None

    locationId: Optional[str] = None
    locationName: Optional[str] = None

    farmId: Optional[str] = None
    farmName: Optional[str] = None

    teamId: Optional[str] = None
    teamName: Optional[str] = None

    firstName: Optional[str] = None
    lastName: Optional[str] = None
    englishName: Optional[str] = None

    bsb: Optional[str] = None
    accountNumber: Optional[str] = None

    email: Optional[str] = None
    cellPhone: Optional[str] = None
    taxFileNumber: Optional[str] = None
    birthDate: Optional[str] = None
    gender: Optional[str] = None
    nationality: Optional[str] = None
    passportNumber: Optional[str] = None
    visaGrantNumber: Optional[str] = None
    fundName: Optional[str] = None
    memberNumber: Optional[str] = None
    address: Optional[str] = None

    startDate: Optional[str] = None
    endDate: Optional[str] = None
    tax: Optional[str] = None
    farmNumber: Optional[str] = None
    memo: Optional[str] = None
