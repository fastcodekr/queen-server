from typing import Optional

from pydantic import BaseModel


class BoardVO(BaseModel):
    id: Optional[str] = None
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None
    title: Optional[str] = None
    content: Optional[str] = None
    companyId: Optional[str] = None
