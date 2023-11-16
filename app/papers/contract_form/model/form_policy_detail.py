from typing import Optional

from pydantic import BaseModel


class FormPolicyDetailVO(BaseModel):
    id: Optional[str] = None
    number: Optional[str] = None
    content: Optional[str] = None
    formPolicyNumber: Optional[str] = None
