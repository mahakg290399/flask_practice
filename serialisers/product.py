
from db import ma
from models.product import ProductModel
from serialisers.category import CategorySchema
from flask_marshmallow.fields import fields

class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ProductModel
        load_instance= True
        fields = ('seller_id', 'product_name', 'product_id', 'price', 'category')
        dump_only = ('product_id',)
        include_relationships = True
    category= fields.Nested(CategorySchema)

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)