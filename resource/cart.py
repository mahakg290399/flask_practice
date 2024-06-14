from flask_restx import Resource
from flask_jwt_extended import jwt_required, get_jwt, get_jwt_identity
from flask import request
from db import db
from models.product import ProductModel
from models.user import UserModel
from serialisers.product import product_schema
from serialisers.cartproduct import cartproduct_schema

class Cart(Resource):
    @jwt_required()
    def post(self):
        role_id = get_jwt()['role_id']
        user:UserModel = UserModel.query.filter_by(user_id = get_jwt_identity()).one_or_none()
        if not(user):
            return {'message', 'Invalid User'}
        if role_id != 2:
            return{'message':'must be a buyer'}
        
        data = request.get_json()
        price = ProductModel.query.filter_by(product_id = data['product_id']).one_or_none().price
        cp = cartproduct_schema.load(data=data)
        cp.total_amount = price*cp.quantity
        db.session.add()
        
        
        
        