import base64, io, json
from typing import Optional
from lib.connection import connection
from fastapi import HTTPException
from src.services.users import models, utils
from src.services.users.serializers import parse_keys

import lib.acl as ACL
from fastapi import Request, Response


async def user_login(user: models.Userlogin, response: Response):
    result = None
    if user.login.isdigit():
        user.login = utils.correct_phone_number(user.login)

    with connection() as cur:
        cur.callproc('"user".check_user', (user.login, user.password))
        result = cur.fetchone()
        result = result[0] if result else None


    # add JWT token
    if result:
        result['jwt_token'] = ACL.sign_token(user.login, result['id'], result['roles'])
        ref_token = ACL.refresh_token(user.login, result['id'], result['roles'])
        response.set_cookie(key="refresh_token", value=ref_token, httponly=True, secure=True)
        return result
    else:
        raise HTTPException(status_code=401, detail="Invalid login or password.")




async def user_registration(user: models.UserReg):
    user.phone_number = utils.correct_phone_number(user.phone_number)

    result = None
    with connection() as cur:
        cur.callproc('"user".add_user',
                    (user.first_name, user.last_name, user.phone_number, user.password, user.role_id, user.middle_name,
                     user.email, user.position_id, user.p_department_id))
        result = cur.fetchone()
        result = result[0] if result else None

    return result


async def update_user(user_id, user, payload):
    result = None
    if user.phone_number:
        user.phone_number = utils.correct_phone_number(user.phone_number)
    with connection() as cur:
        cur.callproc('"user".update_user2',
            (user_id, user.first_name, user.last_name, user.phone_number, user.role_id, user.middle_name,
             user.email, user.position_id, user.department_id, user.disabled, user.active, user.password)
        )
        result = cur.fetchone()
        result = result[0] if result else None

    return result


async def user_logout(device_token: Optional[str]):
    if device_token is not None:
        #user_id = payload['user_id']
        with connection() as cur:
            cur.execute('CALL account.delete_device_token_v3(%s);', [device_token])
    
    return 'success'   


async def update_user_password(passw: models.ChangePassword, payload: dict):
    password_validator = utils.password_check(passw.new_password1)
    if password_validator != 1:
        return password_validator
    login = payload['user_login']
    result = None
    with connection() as cur:
        cur.execute('call account.change_password(%s,%s,%s,%s,%s);',
                    (login, passw.old_password, passw.new_password1, passw.new_password2, '{}'))
        result = cur.fetchone()[0]
       
    return result


async def change_user_password(new_pass):
    result = None
    with connection() as cur:
        cur.callproc('"user".change_password',(new_pass.user_id, new_pass.password))
        result = cur.fetchone()
        result = result[0] if result else None
        
    return result


async def get_all_roles():
    result = None
    with connection() as cur:
        cur.callproc('"user".get_roles', ())
        result = cur.fetchone()
        result = result[0] if result else None
    return result


async def add_role(name):
    result = None
    with connection() as cur:
        cur.callproc('"user".add_role', (name,))
        result = cur.fetchone()
        result = result[0] if result else None
    return result


async def get_accounts():
    result = None
    with connection() as cur:
        cur.callproc('"user".get_accounts',())
        result = cur.fetchone()
        result = result[0] if result else None
    return result
