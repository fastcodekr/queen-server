from typing import Optional

from pydantic import BaseModel


class FormChecklistDetailVO(BaseModel):
    id: Optional[str] = None
    number: Optional[str] = None
    content: Optional[str] = None
    shortName: Optional[str] = None
    formChecklistNumber: Optional[str] = None
