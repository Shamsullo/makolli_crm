from lib.connection import connection


async def add_position(name):
    result = None
    with connection() as cur:
        cur.callproc('"constant".add_position', (name,))
        result = 'ok'
    return result


async def update_position(id, name, disabled):
    result = None
    with connection() as cur:
        cur.callproc('"constant".update_position', (id, name, disabled))
        result = cur.fetchone()
        result = result[0] if result else None
    return result


async def get_all_positions():
    result = None
    with connection() as cur:
        cur.callproc('"constant".get_positions', ())
        result = cur.fetchone()
        result = result[0] if result else None
    return result


async def delete_position(position_id):
    result = None
    with connection() as cur:
        cur.execute('call "constant".delete_position(%s)', (position_id,))
        result = 'ok'

    return result


async def add_department(name):
    result = None
    with connection() as cur:
        cur.callproc('"company".add_department', (name,))
        result = 'ok'
    return result


async def update_department(id, name, disabled):
    result = None
    with connection() as cur:
        cur.callproc('company.update_department', (id, name, disabled))
        result = cur.fetchone()
        result = result[0] if result else None
    return result


async def get_all_departments():
    result = None
    with connection() as cur:
        cur.callproc('company.get_departments', ())
        result = cur.fetchone()
        result = result[0] if result else None
    return result


async def add_client(name, leg_person):
    result = None
    with connection() as cur:
        cur.callproc('company.add_client', (name, leg_person))
        result = cur.fetchone()
        result = result[0] if result else None
    return result


async def update_client(id, name, leg_person, disabled):
    result = None
    with connection() as cur:
        cur.callproc('company.update_client', (id, name, leg_person, disabled))
        result = cur.fetchone()
        result = result[0] if result else None
    return result


async def get_clients():
    result = None
    with connection() as cur:
        cur.callproc('company.get_clients', ())
        result = cur.fetchone()
        result = result[0] if result else None

    return result


async def delete_client(client_id):
    result = None
    with connection() as cur:
        cur.execute('call company.delete_client(%s)', (client_id,))
        result = 'ok'

    return result



async def add_currency(code, short_name, p_rate, full_name=None):
    result = None
    with connection() as cur:
        cur.callproc('"constant".add_currency_with_rate', (code, short_name, p_rate, full_name))
        result = cur.fetchone()
        result = result[0] if result else None

    return result


async def get_currencies():
    result = None
    with connection() as cur:
        cur.callproc('"constant".get_currencies', ())
        result = cur.fetchone()
        result = result[0] if result else None

    return result


async def delete_currency(currency_id):
    result = None
    # with connection() as cur:
    #     cur.execute('call "constant".delete_currency(%s)', (currency_id,))
    #     result = 'ok'

    return result


async def get_employees():
    result = None
    with connection() as cur:
        cur.callproc('company.get_employees', ())
        result = cur.fetchone()
        result = result[0] if result else None

    return result


async def add_cash_accountant_old(user_id, name, currency_id, is_main):
    result = None
    with connection() as cur:
        cur.callproc('company.add_cash_accountant', (name, currency_id, is_main, user_id))
        result = cur.fetchone()
        result = result[0] if result else None
    return result


async def add_cash_accountant(account):
    result = None
    with connection() as cur:
        cur.callproc('company.add_cash_accountant2',
                     (account.name, account.currency_id, account.is_main, account.user_id, account.initial_balance))
        result = cur.fetchone()
        result = result[0] if result else None
    return result


async def update_cash_accountant(id, account):
    result = None
    with connection() as cur:
        cur.callproc(
            'company.update_cash_accountant2',
            (id, account.name, account.currency_id, account.is_main, account.initial_balance, account.disabled)
        )
        result = cur.fetchone()
        result = result[0] if result else None
    return result


async def connect_user_to_cash_account(cash_acc_id, user_ids):
    result = None
    with connection() as cur:
        cur.callproc('company.connect_user_to_cash_accountant2', (cash_acc_id, user_ids))
        result = cur.fetchone()
        result = result[0] if result else None
    return result


async def disconnect_user_to_cash_account(cash_acc_id, user_ids):
    result = None
    with connection() as cur:
        cur.callproc('company.disconnect_user_from_cash_accountant2', (cash_acc_id, user_ids))
        result = cur.fetchone()
        result = result[0] if result else None

    return result


async def get_cash_accountant(user_id):
    result = None
    with connection() as cur:
        cur.callproc('company.get_cash_accountants', [user_id,])
        result = cur.fetchone()
        result = result[0] if result else None

    return result
