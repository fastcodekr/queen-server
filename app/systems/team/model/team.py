from typing import Optional

from pydantic import BaseModel

from app.customers.worker.model.worker import WorkerVO


class TeamVO(BaseModel):
    id: Optional[str] = None
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None
    name: Optional[str] = None
    staffId: Optional[str] = None
    companyId: Optional[str] = None
    workerArray: Optional[list[WorkerVO]] = None
