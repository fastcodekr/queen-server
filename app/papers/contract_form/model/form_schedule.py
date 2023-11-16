from typing import Optional

from pydantic import BaseModel


class FormScheduleVO(BaseModel):
    id: Optional[str] = None
    number: Optional[str] = None
    title: Optional[str] = None
    content1: Optional[str] = None
    content2: Optional[str] = None
    content21: Optional[str] = None
    content22: Optional[str] = None
