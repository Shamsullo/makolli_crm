# /src/services/users/main.py

from src.services.users import crud, models, utils
from typing import Optional
import lib.acl as ACL
from fastapi import Depends, APIRouter, Request, Response, HTTPException

from src.services.users.models import ChangePassword

router = APIRouter(prefix='/user', tags=["Users"])


@router.post('/login')
async def user_login(user: models.Userlogin, response: Response):
    return await crud.user_login(user, response)


@router.post('/registration')
async def user_registration(user: models.UserReg):
    return await crud.user_registration(user)


@router.put('/change_password')
async def change_user_password(new_pas: ChangePassword):
    return await crud.change_user_password(new_pas)


@router.put('/update')
async def update_user(user_id: int, user: models.UserUpdate, payload: dict = Depends(ACL.JWTpayload)):
    return await crud.update_user(user_id, user, payload)

@router.get('/roles')
async def get_all_role_types(c):
    return await crud.get_all_roles()


@router.post('/role')
async def add_role(name):
    return await crud.add_role(name)

@router.get('/accounts')
async def get_accounts(payload: dict = Depends(ACL.JWTpayload)):
    return await crud.get_accounts()
