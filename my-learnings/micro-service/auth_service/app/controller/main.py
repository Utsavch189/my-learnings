from app.db import Transaction
from app.handlers import logger

def get_a_user(email:str)->dict:
    try:
        user={}

        with Transaction() as transaction:
            transaction.execute("SELECT * FROM utsav.user where email='%s'"%(email,))
            res=transaction.fetchone()
            if res:
                user={
                    "id":res[0],
                    "name":res[1],
                    "email":res[2],
                    "password":res[3]
                }
        print(user)
        return user 
    except Exception as e:
        logger.error("get_a_user() | "+repr(e))
        raise Exception("error in get a user")

def add_user(name:str,email:str,password:str)->dict:
    try:
        with Transaction() as transaction:
            transaction.execute("INSERT INTO utsav.user(name,email,password) VALUES('%s','%s','%s')"%(name,email,password))

        user=get_a_user(email)
        if user:
            del user['password']
        return user
    except Exception as e:
        logger.error("add_user() | "+repr(e))
        return {}