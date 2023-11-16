from typing import Optional

from pydantic import BaseModel


class OrderVO(BaseModel):
    id: Optional[str] = None
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None
    farmId: Optional[str] = None
    workerId: Optional[str] = None
