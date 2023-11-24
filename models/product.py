from db import db

class ProductModel(db.Model):
    __tablename__ = "products"
    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(80))
    price = db.Column(db.Integer)
    seller_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    seller = db.relationship("UserModel", back_populates = "products")
    category_id = db.Column(db.Integer, db.ForeignKey("categories.category_id"))
    category = db.relationship("CategoryModel", back_populates="products")

    def __init__(self, product_name, price, seller_id, category_id) -> None:
        self.product_name = product_name
        self.price = price
        self.seller_id = seller_id
        self.category_id = category_id