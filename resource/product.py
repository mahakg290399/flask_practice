from flask_restx import Resource
from flask import request
from models.product import ProductModel
from models.role import RoleModel
from serialisers.product import product_schema, products_schema
from flask_jwt_extended import jwt_required, get_jwt
from db import db


class Product(Resource):
    @jwt_required()
    def post(self):
        role_id = get_jwt()["role_id"]
        role = RoleModel.query.filter_by(role_id=role_id).one_or_404()
        if role and role.role_name.casefold() != "Seller".casefold():
            return {"Message": "Only Seller can register the product"}
        data = product_schema.load(request.get_json())
        product = ProductModel.query.filter_by(
            product_name=data.product_name
        ).one_or_none()
        if product:
            return {"message": "Product already exists or sold by other seller."}
        db.session.add(data)
        db.session.commit()
        return product_schema.dump(data)

    def get(self, product_id):
        product = ProductModel.query.filter_by(product_id=product_id).one_or_none()
        return product_schema.dump(product)

    def get(self):
        if len(request.args) == 0: return {"mesage": "Please pass some data in query args if you want to search something"}
        name = request.args["name"]
        product = ProductModel.query.filter_by(product_name = name).one_or_none()
        return product_schema.dump(product)    

class ProductList(Resource):
    def get(self):
        products = ProductModel.query.all()
        return products_schema.dump(products)
