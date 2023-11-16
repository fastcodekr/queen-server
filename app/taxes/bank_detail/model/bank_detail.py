from typing import Optional

from pydantic import BaseModel


class BankDetailVO(BaseModel):
    id: Optional[str] = None
    bankName: Optional[str] = None
    accountName: Optional[str] = None
    bsb: Optional[str] = None
    accountNumber: Optional[str] = None
    personalDetailId: Optional[str] = None
