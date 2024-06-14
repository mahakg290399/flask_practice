from db import db


class CartProductModel(db.Model):
    __tablename__ = "cartproducts"
    cp_id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer)
    cart_id = db.Column(db.Integer, db.ForeignKey("carts.cart_id"))
    product_id = db.Column(db.Integer, db.ForeignKey("products.product_id"))
