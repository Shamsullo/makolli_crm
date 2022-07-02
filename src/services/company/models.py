from typing import Optional
from pydantic import BaseModel


class CashAccountCreate(BaseModel):
    name: str
    currency_id: int
    is_main: Optional[bool]
    user_id: Optional[int]
    initial_balance: Optional[float]
    is_checking: Optional[bool]


class CashAccountUpdate(BaseModel):
    name: Optional[str]
    currency_id: Optional[int]
    is_main: Optional[bool] = False
    initial_balance: Optional[float]
    disabled: Optional[bool]
    is_checking: Optional[bool]
