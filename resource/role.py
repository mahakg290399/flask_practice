from flask_restx import Resource
from flask import request
from models.role import RoleModel
from serialisers.role import role_schema
from db import db


class Role(Resource):
    def post(self):
        data = role_schema.load(request.get_json())
        print(data)
        role = RoleModel.query.filter_by(role_name = data.role_name).one_or_none()
        if role:
            return {"message":'role already exists'}
        else:
            db.session.add(data)
            db.session.commit()
            return role_schema.dump(data)