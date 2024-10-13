from app_instance import app
from flask import jsonify, request,make_response
from logger_setup import logger
from verify_sign import verify
import random

@app.before_request
def manipulate_data():
    raand=random.randint(1,10)
    if raand==5:
        print("manipulation done!")
        request.json['data']={"message":"data manipulated"}

@app.before_request
def verify_sign():
    try:
        data=request.json
        json_data=data.get('data')
        signature=data.get('signature')
        signed_timestamp=data.get('signed_timestamp')

        if not signature:
            logger.error("signature is missing!")
            response=make_response(jsonify({"message":"signature is missing!"}),400)
            return response
        
        verification=verify(signature,json_data)

        if not verification:
            logger.error(f"signature verification failed! And was signed on {signed_timestamp}")
            response=make_response(jsonify({"message":"signature verification failed!"}),400)
            return response
        
        logger.info(f"signature verification success! And was signed on {signed_timestamp}")
    except Exception as e:
        logger.error(str(e))



@app.route("/api/data",methods=['POST'])
def post_data():
    data=request.json
    print(data)
    return make_response(jsonify({"message":"right data get!","data":data}),200)

if __name__ == '__main__':
    app.run(debug=True)