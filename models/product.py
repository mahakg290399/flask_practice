from db import db


class ProductModel(db.Model):
    __tablename__ = "products"
    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(80))
    price = db.Column(db.Integer)
    seller_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    category_id = db.Column(db.Integer, db.ForeignKey("categories.category_id"))

    seller = db.relationship("UserModel", back_populates="products")
    category = db.relationship("CategoryModel", back_populates="products")

