from typing import Optional

from pydantic import BaseModel, EmailStr
from pydantic.class_validators import List


class AddTransaction(BaseModel):
    date_time: Optional[str] = None
    operation_type_id: int
    source: str
    outgo: Optional[float] = 0.0
    income: Optional[float] = 0.0
    dds_article_id: Optional[int]
    desc: Optional[str]
    client_id: Optional[int]
    employee_id: Optional[int]
    fcash_account_id: Optional[int]
    tcash_account_id: Optional[int]


class UpdateTransaction(BaseModel):
    date_time: Optional[str]
    operation_type_id: Optional[int]
    source: Optional[str]
    outgo: Optional[float]
    income: Optional[float]
    dds_article_id: Optional[int]
    desc: Optional[str]
    client_id: Optional[int]
    employee_id: Optional[int]
    fcash_account_id: Optional[int]
    tcash_account_id: Optional[int]
    user_id: Optional[int]


class ModifyAccess(BaseModel):
    start_date: str
    end_date: str
    user_id: int
    cash_account_id: int


class ReportFilter(BaseModel):
    start_date: str
    end_date: str
    group_by: int
    cash_account_ids: Optional[list]
    income: Optional[bool]
    outgo: Optional[bool]


class EmailModel(BaseModel):
    subject: str
    email: List[EmailStr] #=Query(...),
    body: str
