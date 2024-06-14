from db import ma
from models.cartproduct import CartProductModel

class CartProdcutSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        load_instance = True
        include_fk = True
        include_relationships = True
        dump_only = ('cp_id','quantity')
        model = CartProductModel

cartproduct_schema = CartProdcutSchema()
