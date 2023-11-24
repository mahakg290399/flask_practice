from db import db

class CartModel(db.Model):
    __tablename__ = "carts"

    cart_id = db.Column(db.Integer, primary_key = True)
    total_amount = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    user = db.relationship("UserModel", back_populates = "cart")

