from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.orm import relationship
from app import db

db = SQLAlchemy()

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    order_date = db.Column(db.DateTime, default=datetime.utcnow)
    products = db.Column(db.String(500), nullable=False)  # JSON or comma-separated list
    delivery_time = db.Column(db.String(100), nullable=False)

    user = db.relationship('User', back_populates='orders')

    def __repr__(self):
        return f"<Order {self.id} for User {self.user_id}>"



# # models/order_model.py
# from sqlalchemy.orm import relationship
# from app import db

# class Order(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     # Other fields...

# # models/user_model.py
# from sqlalchemy.orm import relationship
# from app import db
# from models.order_model import Order

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(50), nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     orders = relationship("Order", backref="user")
