from typing import Optional
from pydantic import BaseModel


class Userlogin(BaseModel):
    login: str
    password: str


class UserReg(BaseModel):
    first_name: str
    last_name: str
    middle_name: Optional[str]
    phone_number: str
    password: Optional[str]
    password_repeat: Optional[str]
    email: Optional[str]
    role_id: Optional[int]
    position_id: Optional[int]
    p_department_id: Optional[int]


class UserUpdate(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    middle_name: Optional[str]
    phone_number: Optional[str]
    role_id: Optional[int]
    email: Optional[str]
    position_id: Optional[int]
    department_id: Optional[int]
    disabled: Optional[bool]
    active: Optional[bool]
    password: Optional[str]


class ChangePassword(BaseModel):
    user_id: int
    password: str
