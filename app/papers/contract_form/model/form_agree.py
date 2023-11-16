from typing import Optional

from pydantic import BaseModel


class FormAgreeVO(BaseModel):
    id: Optional[str] = None
    number: Optional[str] = None
    content: Optional[str] = None
