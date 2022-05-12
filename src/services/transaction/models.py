from typing import Optional
from pydantic import BaseModel

class AddTransaction(BaseModel):
    date_time: str
    operation_type_id: int
    source: str
    outgo: Optional[float] = 0.0
    income: Optional[float] = 0.0
    dds_article_id: Optional[int]
    desc: Optional[str]


class UpdateTransaction(BaseModel):
    date_time: Optional[str]
    operation_type_id: Optional[int]
    source: Optional[str]
    outgo: Optional[float]
    income: Optional[float]
    dds_article_id: Optional[int]
    desc: Optional[str]

