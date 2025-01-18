# # import sys
# # import os
# # sys.path.append(os.path.join(os.path.dirname(__file__), 'models'))  # Ensure 'models' folder is added to the path

# from flask import Flask
# from db import db 
# from flask_sqlalchemy import SQLAlchemy

# from flask import request, jsonify

# # Now import from the models package
# from models.product_model import Product
# from models.order_model import Order
# from models.user_model import User



# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kirana_store.db'  # Using SQLite for simplicity
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db.init_app(app)
# # db = SQLAlchemy(app)

# @app.before_first_request
# def create_tables():
#     db.create_all()


# @app.route('/product', methods=['POST'])
# def add_product():
#     data = request.get_json()
#     new_product = Product(name=data['name'], price=data['price'], description=data.get('description', ''), category=data['category'])
#     db.session.add(new_product)
#     db.session.commit()
#     return jsonify({"message": "Product added successfully!"}), 201

# @app.route('/user', methods=['POST'])
# def add_user():
#     data = request.get_json()
#     new_user = User(username=data['username'], email=data['email'])
#     db.session.add(new_user)
#     db.session.commit()
#     return jsonify({"message": "User added successfully!"}), 201

# if __name__ == "__main__":
#     app.run(debug=True)







from flask import Flask
from flask import request, jsonify


from flask_sqlalchemy import SQLAlchemy
from models.product_model import Product
from models.order_model import Order
from models.user_model import User

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kirana_store.db'  # Using SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/')
def home():
    return "Kirana Store Ordering System"

@app.route('/test', methods=['GET'])
def test_route():
    return jsonify({"message": "Test route is working"}), 200


@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/product', methods=['POST'])
def add_product():
    data = request.get_json()
    new_product = Product(name=data['name'], price=data['price'], description=data.get('description', ''), category=data['category'])
    db.session.add(new_product)
    db.session.commit()
    return jsonify({"message": "Product added successfully!"}), 201

@app.route('/user', methods=['POST'])
def add_user():
    data = request.get_json()
    new_user = User(username=data['username'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User added successfully!"}), 201


if __name__ == "__main__":
    app.run(debug=True)

