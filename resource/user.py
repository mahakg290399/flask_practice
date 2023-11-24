from flask_restx import Resource, reqparse, abort
from flask import jsonify
from models.user import UserModel
from flask_jwt_extended import jwt_required, create_access_token
from db import db

class UserRegister(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("username", type=str)
        parser.add_argument("password", type=str)
        parser.add_argument("role_id",type=int)
        args = parser.parse_args()
        username = args['username']
        password = args['password']
        role_id = args['role_id']
        user = UserModel.query.filter_by(user_name = username).one_or_none()
        if user and user.user_name  == username:
            return "User Already exists"
        else:   
            user = UserModel(username, password, role_id)
            db.session.add(user)
            db.session.commit()
        

class UserLogin(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("username", type=str)
        parser.add_argument("password", type=str)
        args = parser.parse_args()
        username = args['username']
        password = args['password']
        user = UserModel.query.filter_by(user_name = username).one_or_none()
        if user:
            return create_access_token(identity=user.user_id, additional_claims={"role":user.role_id})
        else:
            return {"Message": "User is not registered."}
