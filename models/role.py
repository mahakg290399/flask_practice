from db import db


class RoleModel(db.Model):
    __tablename__ = "roles"
    role_id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String)
    users = db.relationship("UserModel", back_populates="role")

  