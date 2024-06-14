from flask import request
from flask_restx import Resource
from flask_jwt_extended import jwt_required, get_jwt
from serialisers.category import category_schema
from models.role import RoleModel
from models.category import CategoryModel
from db import db

class Category(Resource):
    @jwt_required()
    def post(self):
        data = category_schema.load(request.get_json())
        jwt = get_jwt()
        data_role_id = jwt['role_id']
        role = RoleModel.query.filter_by(role_id = data_role_id).one_or_none()
        if role and role.role_id != 1:
            return {
                'message': 'the token does not belong to a seller. Hence login as a seller to add category'
            }
        category:CategoryModel = CategoryModel.query.filter_by(category_name = data.category_name).one_or_none()

        if category and category.category_name.casefold() == data.category_name.casefold():
            return {'message':"Category already exists"}
        else:
            db.session.add(data)
            db.session.commit()
            return category_schema.dump(data)    
        