from typing import Optional

from pydantic import BaseModel

from app.customers.farm.model.farm import FarmVO


class LocationVO(BaseModel):
    id: Optional[str] = None
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None
    name: Optional[str] = None
    farmArray: Optional[list[FarmVO]] = None
