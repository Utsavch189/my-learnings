from flask import Blueprint,jsonify,make_response,request
from app.service import ProductService
from app.security import is_authorize

product_bp = Blueprint('product', __name__)

@product_bp.route("/product/<int:id>",methods=['GET'])
def get_product(id):
    try:
        status,data=ProductService.get_product(id)
        return make_response(jsonify(data),status)
    except Exception as e:
        return make_response(jsonify({"message":"something is wrong!"}),500)

@product_bp.route("/products",methods=['GET'])
def get_products():
    try:
        page = request.args.get('page', default=1, type=int)
        page_size = request.args.get('page_size', default=10, type=int)
        status,data=ProductService.get_products(page,page_size)
        return make_response(jsonify(data),status)
    except Exception as e:
        return make_response(jsonify({"message":"something is wrong!"}),500)

@product_bp.route("/product/create",methods=['POST'])
@is_authorize()
def create_product(**kwargs):
    try:
        json_data=request.json
        status,data=ProductService.create_product(json_data.get('name'),json_data.get('price'))
        return make_response(jsonify(data),status)
    except Exception as e:
        print(e)
        return make_response(jsonify({"message":"something is wrong!"}),500)

@product_bp.route("/product/update",methods=['PUT'])
@is_authorize()
def update_product(**kwargs):
    try:
        json_data=request.json
        status,data=ProductService.update_product(json_data.get('id'),json_data.get('name'),json_data.get('price'))
        return make_response(jsonify(data),status)
    except Exception as e:
        return make_response(jsonify({"message":"something is wrong!"}),500)

@product_bp.route("/product/delete/<int:id>",methods=['DELETE'])
@is_authorize()
def delete_product(id,**kwargs):
    try:
        status,data=ProductService.delete_product(id)
        return make_response(jsonify(data),status)
    except Exception as e:
        return make_response(jsonify({"message":"something is wrong!"}),500)