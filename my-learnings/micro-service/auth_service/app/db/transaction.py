from .config import get_connection
import traceback
import json
from app.handlers import logger

class Transaction:

    def __init__(self,handel_exception_silently:bool=False) -> None:
        self.handel_exception_silently=handel_exception_silently
        try:
            self.conn,self.cursor=get_connection()
        except Exception as e:
            self.conn=None
            self.cursor=None
    
    def __enter__(self):
        return self.cursor
    
    def __exit__(self,exc_type,exc_value,exc_tb):
        if self.conn==None:
            traceback_dict={
                "exception":"Database connection error!"
            }
            logger.error(json.dumps(traceback_dict,indent=4))
            return True
        elif exc_value:
            tb_info=traceback.extract_tb(exc_tb)[0]
            file_name=tb_info.filename
            lineno=tb_info.lineno
            func_name=tb_info.name
            traceback_dict={
                "file":file_name,
                "line":lineno,
                "func":func_name,
                "exception_type":str(exc_type),
                "exception":str(exc_value)
            }
            logger.error(json.dumps(traceback_dict,indent=4))
            self.conn.rollback()
            self.cursor.close()
            self.conn.close()
        else:
            self.conn.commit()
            self.cursor.close()
            self.conn.close()

        if self.handel_exception_silently:
            return True


if __name__=="__main__":
    def func1():
        res=[]
        with Transaction() as cusrsor:
            cusrsor.execute("select * from User;")
            res=cusrsor.fetchall()
        for r in res:
            print(r)
    func1()