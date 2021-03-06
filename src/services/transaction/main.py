from typing import List

from pydantic import EmailStr
from starlette.responses import JSONResponse

from src.services.transaction import crud, models, utils
import lib.acl as ACL
from fastapi import Depends, APIRouter, UploadFile, File, Query
from fastapi_mail import FastMail, MessageSchema,ConnectionConfig

router = APIRouter(prefix='/transaction', tags=["Transactions"])


@router.post('/add')
async def add_transaction(trans: models.AddTransaction, payload: dict = Depends(ACL.JWTpayload)):
    return await crud.add_transaction(trans, payload)


@router.get('/from-to-list')
async def get_from_to_list(payload: dict = Depends(ACL.JWTpayload)):
    return await crud.get_from_to_list(payload)


@router.post('/history')
async def get_transaction_history(start_date, end_date, cash_accountant_ids: List[int]=None, payload: dict = Depends(ACL.JWTpayload)):
    return await crud.get_transaction_history(start_date, end_date, cash_accountant_ids, payload)


@router.put('/update')
async def update_transaction(trans_id: int, trans: models.UpdateTransaction, payload: dict = Depends(ACL.JWTpayload)):
    return await crud.update_transaction(trans_id, trans, payload)


@router.post('/cancel')
async def cancel_transaction(trans_id: int, payload: dict = Depends(ACL.JWTpayload)):
    return await crud.cancel_transaction(trans_id)


@router.post('/access')
async def give_modify_access(access: models.ModifyAccess, payload: dict = Depends(ACL.JWTpayload)):
    return await crud.give_modify_access(access)


@router.delete('/delete')
async def add_position(trans_id: int, payload: dict = Depends(ACL.JWTpayload)):
    return await crud.delete_transaction(trans_id)


@router.post('/operation_type')
async def add_operation_type(name, payload: dict = Depends(ACL.JWTpayload)):
    return await crud.add_operation_type(name)


@router.put('/operation_type')
async def update_operation_type(id: int, name=None, disabled: bool=None, payload: dict = Depends(ACL.JWTpayload)):
    return await crud.update_operation_type(id, name, disabled)


@router.get('/operation_types')
async def get_operation_types(payload: dict = Depends(ACL.JWTpayload)):
    return await crud.get_operation_types()


@router.delete('/operation_type')
async def delete_operation_type(opt_id, payload: dict = Depends(ACL.JWTpayload)):
    return await crud.delete_operation_type(opt_id)


@router.post('/dds_article')
async def add_dds_article(name: str, code: str, desc: str = None, payload: dict = Depends(ACL.JWTpayload)):
    return await crud.add_dds_article(name, code, desc)


@router.get('/dds_articles')
async def get_dds_articles(payload: dict = Depends(ACL.JWTpayload)):
    return await crud.get_dds_articles()


@router.put('/dds_article')
async def update_dds_article(id: int, name: str = None, code: str = None, desc: str = None, disabled: bool = None, payload: dict = Depends(ACL.JWTpayload)):
    return await crud.update_dds_article(id, name, code, desc, disabled)


@router.delete('/dds_article')
async def delete_dds_article(dds_id, payload: dict = Depends(ACL.JWTpayload)):
    return await crud.delete_dds_article(dds_id)


@router.get('/exchange_rate')
async def get_currencies_exchange_rate(p_date=None, payload: dict = Depends(ACL.JWTpayload)):
    return await crud.get_currencies_exchange_rate(p_date)


@router.put('/exchange_rate')
async def update_currency_rate(p_code, p_rate, payload: dict = Depends(ACL.JWTpayload)):
    return await crud.update_currency_rate(p_code, p_rate)


@router.get('/report')
async def get_report_in_excel(payload: dict = Depends(ACL.JWTpayload)):
    return await crud.get_report_in_excel()


@router.get('/report_files')
async def get_reports_location(payload: dict = Depends(ACL.JWTpayload)):
    return await crud.get_list_of_reports_location()


@router.post('/report_json')
async def get_json_data_for_reporting(filter: models.ReportFilter, payload: dict = Depends(ACL.JWTpayload)):
    return await crud.get_json_data_for_reporting(filter)


conf = ConnectionConfig(
    MAIL_USERNAME = "cf@makolli.tj",
    MAIL_PASSWORD = "RaYUcB41%yty",
    MAIL_FROM = "cf@makolli.tj",
    MAIL_PORT = 587,
    MAIL_SERVER = "smtp.mail.ru",
    # MAIL_FROM_NAME="Desired Name",
    MAIL_TLS = True,
    MAIL_SSL = False,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True
)


@router.post('/send_report')
async def send_file(
    subject: str, body: str, email: List[EmailStr]=Query(...),
    file: UploadFile = File(...)
) -> JSONResponse:
    message = MessageSchema(
        subject=subject,
        recipients=email,
        body=body,
        attachments=[file]
    )

    fm = FastMail(conf)
    await fm.send_message(message)
    return JSONResponse(status_code=200, content={"message": "email has been sent"})
