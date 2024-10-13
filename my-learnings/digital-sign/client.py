import requests
from key_generate import generate_keypair 
from create_sign import sign
import time,json
from utility.logger_setup import logger

data={"name":"Utsav"}

if __name__=="__main__":
    generate_keypair()
    final_payload=sign(data)
    while True:
        try:
            url="http://127.0.0.1:5000/api/data"
            res=requests.post(url=url,data=json.dumps(final_payload),headers={"Content-Type":"application/json"})
            print(res)
            if res.status_code == 200:
                data=res.json()
                logger.info(data.get('message'))
            else:
                data=res.json()
                logger.error(data.get('message'))
        except Exception as e:
            logger.error(str(e))
        time.sleep(3)