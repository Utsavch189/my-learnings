from app.handlers import verify_password,JwtBuilder,logger
from app.controller import get_a_user
from typing import Tuple

def login(email,password)->Tuple[bool,dict]:
    try:
        user=get_a_user(email)
        if not user:
            return False,{"message":"user doesn't exists!"}
        hashed_password=user.get('password')
        if not verify_password(password,hashed_password):
            return False,{"message":"password is wrong!"}
        token=JwtBuilder().get_token(
            payload={
                "sub":user.get("name"),
                "email":user.get("email")
            }
        )
        return True,token
    except Exception as e:
        logger.error("login() | "+repr(e))
        raise Exception(str(e))