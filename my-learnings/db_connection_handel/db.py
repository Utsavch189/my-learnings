import mysql.connector
import traceback
import json

class DbCursor:

    def __init__(self) -> None:
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="utsav",
                password="utsav@2001",
                database='utsav',
                port=3306
            )
            self.conn=conn
            self.cursor=self.conn.cursor()
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
            print(json.dumps(traceback_dict,indent=4))
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
            print(json.dumps(traceback_dict,indent=4))
            self.conn.rollback()
            self.cursor.close()
            self.conn.close()
        else:
            self.conn.commit()
            self.cursor.close()
            self.conn.close()
        return True

def func1():
    res=[]
    with DbCursor() as cusrsor:
        cusrsor.execute("select * from User;")
        res=cusrsor.fetchall()
    for r in res:
        print(r)

if __name__=="__main__":
    func1()