from db import ma

class CartSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        load_instace = True
        fields = ('cart_it', 'total_amount', 'user_id')
        