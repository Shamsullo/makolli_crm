from lib.config import static_env
from lib.connection import connection
import openpyxl
from datetime import date
from openpyxl.styles import Font


async def add_transaction(trans, payload):
    result = None
    with connection() as cur:
        cur.callproc('"transaction".add_transaction1', (
            trans.operation_type_id, trans.source, payload['user_id'], trans.outgo,
            trans.income, trans.dds_article_id, trans.desc, trans.date_time,
            trans.client_id, trans.employee_id, trans.fcash_account_id, trans.tcash_account_id
            )
        )
        result = cur.fetchone()
        result = result[0] if result else None

    return result


async def get_from_to_list(payload):
    result = None
    with connection() as cur:
        cur.callproc('transaction.list_of_to_from', ())
        result = cur.fetchone()
        result = result[0] if result else None

    return result


async def get_transaction_history(start_date, end_date, cash_accountant_ids, payload):
    result = None
    with connection() as cur:
        cur.callproc('"transaction".get_transaction1', (start_date, end_date, payload['user_id'], cash_accountant_ids))
        result = cur.fetchone()
        result = result[0] if result else None
    return result


async def update_transaction(trans_id, trans, payload):
    result = None
    with connection() as cur:
        cur.callproc('"transaction".update_transaction1', (
            trans_id, trans.date_time, trans.operation_type_id, trans.source, trans.outgo,
            trans.income, trans.dds_article_id, trans.desc, trans.client_id, trans.employee_id,
            trans.fcash_account_id, trans.tcash_account_id, trans.user_id
            )
        )
        result = cur.fetchone()
        result = result[0] if result else None
    return result


async def cancel_transaction(trans_id):
    result = None
    with connection() as cur:
        cur.callproc('transaction.cancel_transaction', (trans_id,))
        result = cur.fetchone()
        result = result[0] if result else None
    return result


async def give_modify_access(access):
    result = None
    with connection() as cur:
        cur.callproc('transaction.give_modify_access_for_cash_accountant',
            (access.start_date, access.end_date, access.cash_accountant_id, access.user_id)
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


async def update_operation_type(id, name, disabled):
    result = None
    with connection() as cur:
        cur.callproc('"constant".update_operation_type', (id, name, disabled))
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


async def update_dds_article(id, name, code, desc, disabled):
    result = None
    with connection() as cur:
        cur.callproc('"constant".update_dds_article', (id, name, code, desc, disabled))
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


async def get_report_in_excel():
    result = None
    with connection() as cur:
        cur.execute('select "transaction".get_report_data()')
        result = cur.fetchone()
        result = result[0] if result else None

    if result:
        REPORT_FILE_NAME = static_env()['report_path'] + '/report_' + str(date.today()) + '.xlsx'
        report = openpyxl.Workbook()

        sheet = report.active

        sheet['B1'].value = 'Сумма доходов:'
        sheet['B1'].font = Font(bold=True)
        sheet['C1'].value = result['total_income'] if result['total_income'] else 0

        sheet['B2'].value = 'Сумма расходов:'
        sheet['B2'].font = Font(bold=True)
        sheet['C2'].value = result['total_outgo'] if result['total_outgo'] else 0

        sheet['B3'].value = 'Остаток:'
        sheet['B3'].font = Font(bold=True)
        sheet['C3'].value = result['in_bank'] if result['in_bank'] else 0

        sheet['A5'] = 'ID'
        sheet['A5'].font = Font(bold=True)

        sheet['B5'] = 'ДАТА'
        sheet['B5'].font = Font(bold=True)
        sheet.column_dimensions['B'].width = 20

        sheet['C5'] = 'ВИД ОПЕРАЦИИ'
        sheet.column_dimensions['C'].width = 20
        sheet['C5'].font = Font(bold=True)

        sheet['D5'] = 'ПРИХОД'
        sheet['D5'].font = Font(bold=True)

        sheet['E5'] = 'РАСХОД'
        sheet['E5'].font = Font(bold=True)

        sheet['F5'] = 'РАСХОД'
        sheet['F5'].font = Font(bold=True)

        sheet['G5'] = 'КОМУ ВЫДАНО / ОТ КОГО'
        sheet['G5'].font = Font(bold=True)
        sheet.column_dimensions['G'].width = 30

        sheet['H5'] = 'ОСНОВАНИЕ ИЛИ КОММЕНТАРИЙ'
        sheet.column_dimensions['H'].width = 70
        sheet['H5'].font = Font(bold=True)

        sheet['I5'] = 'КАССА'
        sheet['I5'].font = Font(bold=True)

        sheet['J5'] = 'ОТМЕНЕН'
        sheet['J5'].font = Font(bold=True)

        if result['data']:
            row = 7
            for trans in result['data']:
                sheet[row][0].value = trans['id']
                sheet[row][1].value = trans['date_time']
                sheet[row][2].value = trans['ot_name']
                sheet[row][3].value = trans['outgo']
                sheet[row][4].value = trans['income']
                sheet[row][5].value = trans['dds_name']
                sheet[row][6].value = trans['source']
                sheet[row][7].value = trans['desc']
                sheet[row][8].value = trans['fca_name']
                sheet[row][9].value = ('Да' if trans['canceled'] else 'Нет')
                row += 1

        report.save(REPORT_FILE_NAME)
        report.close()

        with connection() as cur:
            cur.execute('call transaction.archive_and_clean_the_logs()')
        return REPORT_FILE_NAME
    return result