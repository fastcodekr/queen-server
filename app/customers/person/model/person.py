from typing import Optional

from pydantic import BaseModel

from app.customers.person.model.passport import PassportVO
from app.customers.worker.model.worker import WorkerVO


class PersonVO(BaseModel):
    id: Optional[str] = None
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None
    title: Optional[str] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    englishName: Optional[str] = None
    gender: Optional[str] = None
    birthDate: Optional[str] = None
    passport: Optional[PassportVO] = None
    workerArray: Optional[list[WorkerVO]] = None
