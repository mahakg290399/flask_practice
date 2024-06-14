from db import ma
from models.role import RoleModel

class RoleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        fields = ('role_id', 'role_name')
        model = RoleModel
        dump_only = ('role_id',)
        load_instance = True

role_schema = RoleSchema()
roles_schema = RoleSchema(many=True)