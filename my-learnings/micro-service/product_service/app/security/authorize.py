from app.handlers import decode
from flask import jsonify,make_response,request
from functools import wraps

def is_authorize(optional=False):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            auth_header = request.headers.get('Authorization')

            if not auth_header and not optional:
                return make_response(jsonify({"message": "Unauthorized!"}), 401)

            if not auth_header.startswith('Bearer '):
                return make_response(jsonify({"message": "Unauthorized!"}), 401)

            token = auth_header.split(' ')[1]
            payload = decode(token)

            if optional:
                _payload=payload if payload else {}
                kwargs['payload'] = _payload
                return func(*args, **kwargs)
            
            if not payload:
                return make_response(jsonify({"message": "Unauthorized!"}), 401)
            
            kwargs['payload'] = payload
            return func(*args, **kwargs)
        return inner
    return wrapper