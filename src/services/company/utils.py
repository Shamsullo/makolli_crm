import random
from lib.connection import connection


# function for connecting phone number format
def correct_phone_number(phone_number):
    if len(phone_number) == 9:
        phone_number = '992' + phone_number
    elif phone_number[0] == '+':
        phone_number = phone_number[1:]
    return phone_number


async def generate_password():
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'

    all = lower + upper + numbers
    length = 9
    password = ''.join(random.sample(all, length))
    return password


def transliterate(name):
   glossary = {'а':'a','б':'b','в':'v','г':'g','д':'d','е':'e','ё':'yo',
      'ж':'zh','з':'z','и':'i','й':'i','к':'k','л':'l','м':'m','н':'n',
      'о':'o','п':'p','р':'r','с':'s','т':'t','у':'u','ф':'f','х':'h',
      'ц':'c','ч':'ch','ш':'sh','щ':'sch','ъ':'','ы':'y','ь':'','э':'e',
      'ю':'u','я':'ya', 'А':'A','Б':'B','В':'V','Г':'G','Д':'D','Е':'E','Ё':'YO',
      'Ж':'ZH','З':'Z','И':'I','Й':'I','К':'K','Л':'L','М':'M','Н':'N',
      'О':'O','П':'P','Р':'R','С':'S','Т':'T','У':'U','Ф':'F','Х':'H',
      'Ц':'C','Ч':'CH','Ш':'SH','Щ':'SCH','Ъ':'','Ы':'y','Ь':'','Э':'E',
      'Ю':'U','Я':'YA',',':'','?':'',' ':'_','~':'','!':'','@':'','#':'',
      '$':'','%':'','^':'','&':'','*':'','(':'',')':'','-':'','=':'','+':'',
      ':':'',';':'','<':'','>':'','\'':'','"':'','\\':'','/':'','№':'',
      '[':'',']':'','{':'','}':'','ґ':'','ї':'', 'є':'','Ґ':'g','Ї':'i',
      'Є':'e', '—':''}
   for key in glossary:
      name = name.replace(key, glossary[key])
   return name


def generate_username(first_name, last_name):
    trans_fname = transliterate(first_name).lower()
    trans_lname = transliterate(last_name).lower()
    username = trans_fname + '_' + trans_lname

    with connection() as cur:

        while(username_exist == True):
            rand_num = random.randint(1000, 9999)
            username.replace(username[-4:], rand_num)

            cur.callproc('account.login_exist', (username,))
            username_exist = cur.fetchall()
            username_exist = username_exist[0][0]

    return username


DB_CON_AND_PY_ERROR = {
        'code': 4,
        'message': "couldn't connect with the database or there is python syntax/runtime error"
    }


def password_check(password):
    r_json = {'status_code': 13, 'message': 'password must be at least 6 character'}
    if len(password) < 6:
        return r_json  
    else:
        return 1

