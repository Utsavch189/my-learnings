from flask import Blueprint,jsonify,make_response,request
from app.service import register

register_bp = Blueprint('register', __name__)

@register_bp.route('/register',methods=['POST'])
def register_router():
    try:
        data=request.json
        response=register(data.get('name'),data.get('email'),data.get('password'))
        return make_response(jsonify(response),201)
    except Exception as e:
        return make_response(jsonify({"message":"something is wrong!"}),500)