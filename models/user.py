from db import db


class UserModel(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)
    role_id = db.Column(db.Integer, db.ForeignKey("roles.role_id"))
    role = db.relationship("RoleModel", back_populates="users")
    cart = db.relationship("CartModel", back_populates="user")
    products = db.relationship("ProductModel", back_populates="seller")
