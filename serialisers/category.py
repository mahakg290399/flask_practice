from models.category import CategoryModel
from db import ma

class CategorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        load_instance = True
        model = CategoryModel
        fields = ('category_name', 'category_id')
        include_fk = True
        dump_only = ('category_id', )

category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)