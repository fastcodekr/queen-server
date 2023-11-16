from typing import Optional

from pydantic import BaseModel


class FormGuidelineVO(BaseModel):
    id: Optional[str] = None
    number: Optional[str] = None
    title: Optional[str] = None
    content: Optional[str] = None
