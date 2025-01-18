from flask_sqlalchemy import SQLAlchemy
from .order_model import Order 

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    orders = db.relationship('Order', back_populates='user')

    def __repr__(self):
        return f"<User {self.username}>"
