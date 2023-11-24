from db import db

class  RoleModel(db.Model):
    __tablename__ = 'roles'
    role_id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String)
    users = db.relationship("UserModel", back_populates="role")

    def __init__(self, role_name):
        self.role_name = role_name

    def __repr__(self):
        return {
            "role_id": self.role_id,
            "role_name": self.role_name
        }
    @classmethod
    def getRoleName(role_id):
        role_name = db.query.filter_by(role_id=role_id).one_or_none().role_name
        if role_name: return role_name
        return "Role Not Found"