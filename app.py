from flask import Flask, jsonify
from flask_restx import Api
from flask_jwt_extended import JWTManager
from resource.user import UserRegister, UserLogin
from resource.product import Product, ProductList
from resource.role import Role
from resource.category import Category
from resource.cart import Cart
from db import db, ma


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = "Mahak"

api:Api = Api(app)
jwt = JWTManager(app)

api.add_resource(UserLogin, "/login")
api.add_resource(UserRegister, "/register")
api.add_resource(Product, "/addproduct")
api.add_resource(Role, "/addrole")
api.add_resource(Category, '/addcategory')
api.add_resource(Product, '/getproduct/<int:product_id>')
api.add_resource(ProductList, '/getproducts')
api.add_resource(Product, '/public/product/search')
api.add_resource(Cart, '/consumer/cart')

@jwt.expired_token_loader
def return_message(header, token):
    return jsonify({"message": "You token has expired"})

db.init_app(app=app)
ma.init_app(app=app)
with app.app_context():
    db.create_all()

app.run(debug=True)
