import os
import psycopg2
from dotenv import load_dotenv
from app.handlers import logger

load_dotenv()

db_host = os.getenv("DB_HOST")
prod_db_host = os.getenv("PROD_DB_HOST")
db_port = os.getenv("DB_PORT")
prod_db_port= os.getenv("PROD_DB_PORT")
user_name = os.getenv("DB_USER")
pass_word = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")
env=os.getenv('ENV')

def get_local_connection():
    try:
        con = psycopg2.connect(
            database=db_name,
            user=user_name,
            password=pass_word,
            host=db_host,
            port=db_port
        )
        cursor = con.cursor()
        return con, cursor
    except Exception as e:
        raise Exception(str(e))
    
def get_prod_connection():
    try:
        con = psycopg2.connect(
            database=db_name,
            user=user_name,
            password=pass_word,
            host=prod_db_host,
            port=prod_db_port
        )
        cursor = con.cursor()
        return con, cursor
    except Exception as e:
        raise Exception(str(e))

def get_connection():
    try:
        if env=='prod':
            return get_prod_connection()
        else:
            return get_local_connection()
    except Exception as e:
        logger.error("get_connection() | ",repr(e))
        return None,None
