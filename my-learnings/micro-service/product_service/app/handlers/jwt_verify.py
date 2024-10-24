import jwt
import os
from dotenv import load_dotenv

load_dotenv()

def decode(token:str) -> dict:
    try:
        return jwt.decode(token,os.getenv('JWT_SECRET'),algorithms=[os.getenv('JWT_ALGORITHM')])
    except Exception as e:
        print(e)
        return {}
