from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)
    availability = db.Column(db.Boolean, default=True)
    description = db.Column(db.String(255), nullable=True)
    category = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Product {self.name}>"
