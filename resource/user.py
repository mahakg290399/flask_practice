from flask_restx import Resource
from flask import request, jsonify
from models.user import UserModel
from models.cart import CartModel
from serialisers.user import user_schema
from flask_jwt_extended import create_access_token
from db import db
from datetime import datetime, timedelta

class UserRegister(Resource):
    def post(self):
        rx_user: UserModel = user_schema.load(request.get_json())
        user: UserModel = UserModel.query.filter_by(
            username=rx_user.username
        ).one_or_none()
        print(user)
        if user and user.username == rx_user.username:
            return {"Message": "User Already exists"}
        else:
            db.session.add(rx_user)
            db.session.commit()
            user_id = UserModel.query.filter_by(user_id = rx_user.user_id).one_or_none().user_id
            cart = CartModel(user_id)
            db.session.add(cart)
            db.session.commit()
            return user_schema.dump(rx_user)


class UserLogin(Resource):
    def post(self):
        data: UserModel = user_schema.load(request.get_json())
        user: UserModel = UserModel.query.filter_by(
            username=data.username
        ).one_or_none()
        if user and data.password == user.password:
            return {
                "access_toekn": create_access_token(
                    identity=user.user_id, expires_delta= timedelta(300),additional_claims={"role_id": user.role_id}
                )
            }
        else:
            return {"Message": "User is not registered."}
