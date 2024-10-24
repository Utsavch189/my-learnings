from app.handlers import password_hash,JwtBuilder,logger
from app.controller import add_user

def register(name,email,password)->dict:
    try:
        user=add_user(name,email,password_hash(password))
        if not user:
            raise Exception("something is wrong in registration!")
        token=JwtBuilder().get_token(
            payload={
                "sub":user.get("name"),
                "email":user.get("email")
            }
        )
        return {"user":user,"token":token}
    except Exception as e:
        logger.error("register() | "+repr(e))
        raise Exception(str(e))