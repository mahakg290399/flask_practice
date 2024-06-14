from db import db


class CategoryModel(db.Model):
    __tablename__ = "categories"
    category_id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String)
    products = db.relationship("ProductModel", back_populates="category")