from app.controller import get_a_product,get_all_products,create_product,update_product,delete_product
from typing import List,Tuple

class ProductService:

    @staticmethod
    def get_product(id:int)->Tuple[int,dict]:
        return 200,get_a_product(id)
    
    @staticmethod
    def get_products(page:int,page_size:int)->Tuple[int,List[dict]]:
        offset=(page - 1) * page_size
        limit=page_size
        return 200,get_all_products(limit,offset)

    @staticmethod
    def create_product(name:str,price:int|float)->Tuple[int,dict]:
        return 201,create_product(name,price)
    
    @staticmethod
    def update_product(id:int,name:str,price:int|float)->Tuple[int,dict]:
        if not get_a_product(id):
            return 400,{"message":"product doesn't exists!"}
        return 200,update_product(id,name,price)
    
    @staticmethod
    def delete_product(id:int)->Tuple[int,dict]:
        delete_product(id)
        return 200,{"message":"deleted!"}