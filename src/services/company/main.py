# /src/services/users/main.py
from pydantic.class_validators import List

from src.services.company import crud, models, utils
import lib.acl as ACL
from fastapi import Depends, APIRouter, Request, Response, HTTPException


router = APIRouter(prefix='/company', tags=["Company"])


@router.post('/position')
async def add_position(name: str, payload: dict = Depends(ACL.JWTpayload)):
    return await crud.add_position(name)


@router.put('/position')
async def update_position(id: int, name: str=None, disabled: bool=None, payload: dict = Depends(ACL.JWTpayload)):
    return await crud.update_position(id, name, disabled)


@router.get('/positions')
async def get_all_role_types(payload: dict = Depends(ACL.JWTpayload)):
    return await crud.get_all_positions()


@router.delete('/position')
async def delete_position(position_id: int, payload: dict = Depends(ACL.JWTpayload)):
    return await crud.delete_position(position_id)


@router.post('/department')
async def add_department(name: str, payload: dict = Depends(ACL.JWTpayload)):
    return await crud.add_department(name)


@router.put('/department')
async def update_department(id: int, name: str = None, disabled: bool = None, payload: dict = Depends(ACL.JWTpayload)):
    return await crud.update_department(id, name, disabled)


@router.get('/departments')
async def get_all_role_types(payload: dict = Depends(ACL.JWTpayload)):
    return await crud.get_all_departments()


@router.post('/client')
async def add_client(name: str, leg_person: bool, payload: dict = Depends(ACL.JWTpayload)):
    return await crud.add_client(name, leg_person)


@router.put('/client')
async def update_client(id: int, name: str=None, leg_person: bool=None, disabled: bool=None, payload: dict = Depends(ACL.JWTpayload)):
    return await crud.update_client(id, name, leg_person, disabled)


@router.get('/clients')
async def get_clients(payload: dict = Depends(ACL.JWTpayload)):
    return await crud.get_clients()


@router.delete('/client')
async def delete_client(client_id: int, payload: dict = Depends(ACL.JWTpayload)):
    return await crud.delete_client(client_id)


@router.post('/currency')
async def add_currency(code, short_name, p_rate, full_name=None, payload: dict = Depends(ACL.JWTpayload)):
    return await crud.add_currency(code, short_name, p_rate, full_name)


@router.get('/currencies')
async def get_clients(payload: dict = Depends(ACL.JWTpayload)):
    return await crud.get_currencies()


@router.delete('/currency')
async def delete_currency(currency_id: int, payload: dict = Depends(ACL.JWTpayload)):
    return await crud.delete_currency(currency_id)


@router.get('/employees')
async def get_employees(payload: dict = Depends(ACL.JWTpayload)):
    return await crud.get_employees()


@router.post('/cash_accountant_old')
async def add_cash_accountant_old(name: str, currency_id: int, is_main: bool, user_id: int = None, payload: dict = Depends(ACL.JWTpayload)):
    return await crud.add_cash_accountant_old(user_id, name, currency_id, is_main)


@router.post('/cash_accountant')
async def add_cash_accountant(account: models.CashAccountCreate, payload: dict = Depends(ACL.JWTpayload)):
    return await crud.add_cash_accountant(account)


@router.put('/cash_accountant')
async def update_cash_accountant(id: int, account: models.CashAccountUpdate, payload: dict = Depends(ACL.JWTpayload)):
    return await crud.update_cash_accountant(id, account)


@router.post('/cash_acc/con')
async def connect_user_to_cash_account(cash_acc_id: int, user_ids: List[int]):
    return await crud.connect_user_to_cash_account(cash_acc_id, user_ids)


@router.post('/cash_acc/dis')
async def disconnect_user_to_cash_account(cash_acc_id: int, user_ids: List[int]):
    return await crud.disconnect_user_to_cash_account(cash_acc_id, user_ids)


@router.get('/cash_accountants')
async def get_cash_accountant(payload: dict = Depends(ACL.JWTpayload)):
    return await crud.get_cash_accountant()
