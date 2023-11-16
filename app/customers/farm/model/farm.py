from typing import Optional

from pydantic import BaseModel

from app.orders.order.model.order import OrderVO


class FarmVO(BaseModel):
    id: Optional[str] = None
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None
    name: Optional[str] = None
    locationId: Optional[str] = None
    companyId: Optional[str] = None
    orderArray: Optional[list[OrderVO]] = None
