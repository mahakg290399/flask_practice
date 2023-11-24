from flask_restx import Resource, reqparse
from flask import jsonify
from models import ProductModel, RoleModel
from flask_jwt_extended import jwt_required , get_jwt
from db import db


class Product(Resource):
    @jwt_required()
    def post(self):
        role_id = get_jwt()['role']
        role = RoleModel.query.filter_by(role_id = role_id).one_or_404()
        print(role.role_name)
        if role and role.role_name != "Seller":
            return "Only Seller can register the product"
        parser = reqparse.RequestParser()
        parser.add_argument("product_name", type=str)
        parser.add_argument("price", type=int)
        parser.add_argument("seller_id", type=int)
        parser.add_argument("category_id",type=int)
        args = parser.parse_args()
        product = ProductModel(args["product_name"], args['price'], args['seller_id'], args['category_id'])
        db.session.add(product)
        db.session.commit()
        