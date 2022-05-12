# /src/services/users/main.py

from src.services.company import crud, models, utils
import lib.acl as ACL
from fastapi import Depends, APIRouter, Request, Response, HTTPException


router = APIRouter(prefix='/company', tags=["Company"])


@router.post('/position')
async def add_position(name: str, payload: dict = Depends(ACL.JWTpayload)):
    return await crud.add_position(name)


@router.get('/positions')
async def get_all_role_types(payload: dict = Depends(ACL.JWTpayload)):
    return await crud.get_all_positions()


@router.delete('/position')
async def delete_position(position_id: int, payload: dict = Depends(ACL.JWTpayload)):
    return await crud.delete_position(position_id)


@router.post('/department')
async def add_department(name: str, payload: dict = Depends(ACL.JWTpayload)):
    return await crud.add_department(name)


@router.get('/departments')
async def get_all_role_types(payload: dict = Depends(ACL.JWTpayload)):
    return await crud.get_all_departments()


@router.post('/client')
async def add_client(name: str, leg_person: bool, payload: dict = Depends(ACL.JWTpayload)):
    return await crud.add_client(name, leg_person)


@router.get('/clients')
async def get_clients(payload: dict = Depends(ACL.JWTpayload)):
    return await crud.get_clients()


@router.delete('/client')
async def delete_client(client_id: int, payload: dict = Depends(ACL.JWTpayload)):
    return await crud.delete_client(client_id)


@router.post('/currency')
async def add_currency(short_name, full_name=None, payload: dict = Depends(ACL.JWTpayload)):
    return await crud.add_currency(short_name, full_name)


@router.get('/currencies')
async def get_clients(payload: dict = Depends(ACL.JWTpayload)):
    return await crud.get_currencies()


@router.delete('/currency')
async def delete_currency(currency_id: int, payload: dict = Depends(ACL.JWTpayload)):
    return await crud.delete_currency(currency_id)


@router.get('/employees')
async def get_employees(payload: dict = Depends(ACL.JWTpayload)):
    return await crud.get_employees()


@router.post('/cash_accountant')
async def add_client(user_id: int, name: str, currency_id: int, is_main: bool, payload: dict = Depends(ACL.JWTpayload)):
    return await crud.add_cash_accountant(user_id, name, currency_id, is_main)
