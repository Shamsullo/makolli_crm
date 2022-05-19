from lib.connection import connection



async def add_transaction(trans, payload):
    result = None
    with connection() as cur:
        cur.callproc('"transaction".add_transaction', (
            trans.operation_type_id, trans.source, payload['user_id'], trans.outgo,
            trans.income, trans.dds_article_id, trans.desc, trans.date_time
            )
        )
        result = cur.fetchone()
        result = result[0] if result else None

    return result


async def get_transaction_history(start_date, end_date, cash_accountant_ids, payload):
    result = None
    with connection() as cur:
        cur.callproc('"transaction".get_transaction', (start_date, end_date, cash_accountant_ids))
        result = cur.fetchone()
        result = result[0] if result else None
    return result


async def get_transaction_history_main(start_date, end_date, cash_accountant_ids, payload):
    result = None
    with connection() as cur:
        cur.callproc('"transaction".get_transaction_main', (start_date, end_date, cash_accountant_ids))
        result = cur.fetchone()
        result = result[0] if result else None
    return result


async def update_transaction(trans_id, trans, payload):
    result = None
    with connection() as cur:
        cur.callproc('"transaction".update_transaction', (
            trans_id, trans.date_time, trans.operation_type_id, trans.source, trans.outgo,
            trans.income, trans.dds_article_id, trans.desc
            )
        )
        result = cur.fetchone()
        result = result[0] if result else None
    return result


async def delete_transaction(trans_id):
    result = None
    with connection() as cur:
        cur.execute('call transaction.delete_transaction(%s)', (trans_id,))
        result = 'ok'
    return result


async def add_operation_type(name):
    result = None
    with connection() as cur:
        cur.callproc('"constant".add_operation_type', (name,))
        result = cur.fetchone()
        result = result[0] if result else None
    return result


async def get_operation_types():
    result = None
    with connection() as cur:
        cur.callproc('"constant".get_operation_types', ())
        result = cur.fetchone()
        result = result[0] if result else None
    return result


async def delete_operation_type(opt_id):
    result = None
    with connection() as cur:
        cur.execute('call "constant".delete_operation_type(%s)', (opt_id,))
        result = 'ok'
    return result


async def add_dds_article(name, code, desc):
    result = None
    with connection() as cur:
        cur.callproc('"constant".add_dds_article', (name, code, desc))
        result = cur.fetchone()
        result = result[0] if result else None
    return result


async def get_dds_articles():
    result = None
    with connection() as cur:
        cur.callproc('"constant".get_dds_articles', ())
        result = cur.fetchone()
        result = result[0] if result else None
    return result


async def delete_dds_article(dds_id):
    result = None
    with connection() as cur:
        cur.execute('call "constant".delete_dds_article(%s)', (dds_id,))
        result = 'ok'
    return result


async def get_currencies_exchange_rate(p_date):
    result = None
    with connection() as cur:
        cur.callproc('transaction.get_currencies_with_rate', (p_date,))
        result = cur.fetchone()
        result = result[0] if result else None

    return result


async def update_currency_rate(p_code, p_rate):
    result = None
    with connection() as cur:
        cur.callproc('transaction.update_currency_rate', (p_code, p_rate,))
        result = cur.fetchone()
        result = result[0] if result else None

    return result