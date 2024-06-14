from db import ma
from models.user import UserModel


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        fields = ("username", "role_id", "password", "user_id")
        model = UserModel
        load_instance = True
        load_only = ("password",)


user_schema = UserSchema()
users_schema = UserSchema(many=True)
