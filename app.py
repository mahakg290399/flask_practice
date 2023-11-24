from flask import Flask
from flask_restx import Api
from db import db
from flask_jwt_extended import JWTManager
from resource.user import UserRegister, UserLogin
from resource.product import Product



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'Mahak'

api = Api(app)
jwt = JWTManager(app)


api.add_resource(UserLogin, '/login')
api.add_resource(UserRegister, '/register')
api.add_resource(Product, "/product")

db.init_app(app=app)
with app.app_context():
    db.create_all()

app.run(debug=True)