from flask import Blueprint,jsonify,make_response,request
from app.service import login

login_bp = Blueprint('login', __name__)

@login_bp.route('/login',methods=['POST'])
def login_router():
    try:
        data=request.json
        status,response=login(data.get('email'),data.get('password'))
        if not status:
            return make_response(jsonify(response),400)
        return make_response(jsonify(response),200)
    except Exception as e:
        return make_response(jsonify({"message":"something is wrong!"}),500)