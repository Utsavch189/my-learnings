import bcrypt

def password_hash(password:str)->str:
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password.decode('utf-8')

def verify_password(password:str,hashed_password:str)->bool:
    if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
        return True
    else:
        return False
    
if __name__=="__main__":
    #print(password_hash("utsav")) # $2b$12$amkVyBDwLjihrWkTFzFnge.M/9I8KwQzpTV5Kko1qwOenKU5yZis6
    print(verify_password("utsav","$2b$12$amkVyBDwLjihrWkTFzFnge.M/9I8KwQzpTV5Kko1qwOenKU5yZis6"))