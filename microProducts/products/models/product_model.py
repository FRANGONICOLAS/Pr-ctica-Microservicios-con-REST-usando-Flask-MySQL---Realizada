from db.db import db

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.String(100), unique=True, nullable=False)
    origin = db.Column(db.String(100), unique=True, nullable=False)

    def __init__(self, product_name, price, origin):
        self.product_name = product_name
        self.price = price
        self.origin = origin

