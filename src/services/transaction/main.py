from typing import List

from src.services.transaction import crud, models, utils
import lib.acl as ACL
from fastapi import Depends, APIRouter, Request, Response, HTTPException

router = APIRouter(prefix='/transaction', tags=["Transactions"])

@router.post('/add')
async def add_transaction(trans: models.AddTransaction, payload: dict = Depends(ACL.JWTpayload)):
    return await crud.add_transaction(trans, payload)


@router.post('/history')
async def get_transaction_history(start_date, end_date, cash_accountant_ids: List[int], payload: dict = Depends(ACL.JWTpayload)):
    return await crud.get_transaction_history(start_date, end_date, cash_accountant_ids, payload)


@router.post('/history_main')
async def get_transaction_history_main(start_date, end_date, cash_accountant_ids: List[int], payload: dict = Depends(ACL.JWTpayload)):
    return await crud.get_transaction_history_main(start_date, end_date, cash_accountant_ids, payload)


@router.put('/update')
async def update_transaction(trans_id: int, trans: models.UpdateTransaction, payload: dict = Depends(ACL.JWTpayload)):
    return await crud.update_transaction(trans_id, trans, payload)


@router.delete('/delete')
async def add_position(trans_id: int, payload: dict = Depends(ACL.JWTpayload)):
    return await crud.delete_transaction(trans_id)


@router.post('/operation_type')
async def add_operation_type(name, payload: dict = Depends(ACL.JWTpayload)):
    return await crud.add_operation_type(name)


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


@router.delete('/dds_article')
async def delete_dds_article(dds_id, payload: dict = Depends(ACL.JWTpayload)):
    return await crud.delete_dds_article(dds_id)

@router.get('/exchange_rate')
async def get_currencies_exchange_rate(p_date=None, payload: dict = Depends(ACL.JWTpayload)):
    return await crud.get_currencies_exchange_rate(p_date)


@router.put('/exchange_rate')
async def update_currency_rate(p_code, p_rate, payload: dict = Depends(ACL.JWTpayload)):
    return await crud.update_currency_rate(p_code, p_rate)
