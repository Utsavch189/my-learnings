from flask import Flask,jsonify,abort
import time

app=Flask(__name__)

@app.route('/simple-api',methods=['GET'])
def simple_api():
    return jsonify({"message":"hello I am simple api!"}),200

@app.route('/complex-api',methods=['GET'])
def complex_api():
    try:
        time.sleep(10) # -- simulate time taken process
        return jsonify({"message":"hello I am complex api!"}),200
    except Exception as e:
        return jsonify({"message":str(e)}),500

if __name__=="__main__":
    app.run()