from typing import Optional

from pydantic import BaseModel


class SuperannuationVO(BaseModel):
    id: Optional[str] = None
    fundName: Optional[str] = None
    memberNumber: Optional[str] = None
    personalDetailId: Optional[str] = None
