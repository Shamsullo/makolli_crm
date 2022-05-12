from lib.config import configdb
from fastapi import HTTPException
from psycopg2 import pool
from contextlib import contextmanager


pg_pool = pool.ThreadedConnectionPool(1, 50, **configdb())

@contextmanager
def connection():
    try:
        #con = connect()
        con = pg_pool.getconn()
        cur = con.cursor()
        yield cur
        con.commit()
    except Exception as e:
        con.rollback()
        cur.close()
        #pg_pool.putconn(con)
        print("db error: {}".format(e))
        raise HTTPException(status_code=409, detail="db error: {}".format(e))
    finally:
        #con.close()
        cur.close()
        pg_pool.putconn(con)
