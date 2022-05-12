from lib.connection import connection


async def add_position(name):
    result = None
    with connection() as cur:
        cur.callproc('"constant".add_position', (name,))
        result = 'ok'

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
        cur.execute('"constant".delete_position(%s)', (position_id,))
        result = 'ok'

    return result


async def add_department(name):
    result = None
    with connection() as cur:
        cur.callproc('"company".add_department', (name,))
        result = 'ok'

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



async def add_currency(short_name, full_name=None):
    result = None
    with connection() as cur:
        cur.callproc('"constant".add_currency', (short_name, full_name))
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
    with connection() as cur:
        cur.execute('call "constant".delete_currency(%s)', (currency_id,))
        result = 'ok'

    return result


async def get_employees():
    result = None
    with connection() as cur:
        cur.callproc('company.get_employees', ())
        result = cur.fetchone()
        result = result[0] if result else None

    return result


async def add_cash_accountant(user_id, name, currency_id, is_main):
    result = None
    with connection() as cur:
        cur.callproc('company.add_cash_accountant', (name, currency_id, is_main, user_id))
        result = cur.fetchone()
        result = result[0] if result else None

    return result