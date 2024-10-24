from app.db import Transaction
from app.handlers import logger
from typing import List

def get_a_product(id:int)->dict:
    try:
        product={}
        with Transaction() as transaction:
            transaction.execute("select * from utsav.product where id=%d;"%(id,))
            _product=transaction.fetchone()
            product['id']=_product[0]
            product['name']=_product[1]
            product['price']=_product[2]
        return product
    except Exception as e:
        logger.error("get_a_product() | ",repr(e))
        raise Exception("something is wrong in product fetching!")


def get_all_products(limit:int,offset:int)->List[dict]:
    try:
        products=[]
        with Transaction() as transaction:
            transaction.execute("select * from utsav.product limit %d offset %d;"%(limit,offset))
            _products=transaction.fetchall()
            products=[{"id":p[0],"name":p[1],"price":p[2]} for p in _products]
        return products
    except Exception as e:
        logger.error("get_all_products() | ",repr(e))
        raise Exception("something is wrong in products fetching!")

def create_product(name:str,price:float|int)->dict:
    try:
        product={}
        with Transaction() as transaction:
            transaction.execute("insert into utsav.product(name,price) values('%s','%s') RETURNING *;"%(name,price))
            _product=transaction.fetchone()
            product['id']=_product[0]
            product['name']=_product[1]
            product['price']=_product[2]
        return product
    except Exception as e:
        logger.error("create_product() | ",repr(e))
        raise Exception("something is wrong in product creating!")

def update_product(id:int,name:str,price:float|int)->dict:
    try:
        product={}
        with Transaction() as transaction:
            transaction.execute("update utsav.product set name='%s', price='%s' where id=%d;"%(name,price,id))
        product=get_a_product(id)
        return product
    except Exception as e:
        logger.error("update_product() | ",repr(e))
        raise Exception("something is wrong in product updating!")

def delete_product(id:int)->dict:
    try:
        with Transaction() as transaction:
            transaction.execute("delete from utsav.product where id=%d;"%(id,))
    except Exception as e:
        logger.error("delete_product() | ",repr(e))
        raise Exception("problem in deleting a product!")