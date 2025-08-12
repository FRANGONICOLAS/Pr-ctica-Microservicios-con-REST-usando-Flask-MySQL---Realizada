from flask import Blueprint, request, jsonify
from products.models.product_model import Products
from db.db import db

product_controller = Blueprint('product_controller', __name__)

@product_controller.route('/api/products', methods=['GET'])
def get_products():
    print("listado de productos")
    products = Products.query.all()
    result = [{'id':product.id, 'product_name': product.product_name, 'price': product.price, 'origin': product.origin} for product in products]
    return jsonify(result)

# Get single user by id
@product_controller.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    print("obteniendo producto")
    product = Products.query.get_or_404(product_id)
    return jsonify({'id': product.id, 'product_name': product.product_name, 'price': product.price, 'origin': product.origin})

@product_controller.route('/api/products', methods=['POST'])
def create_product():
    print("creando producto")
    data = request.json
    #new_user = Users(product_name="oscar", email="oscar@gmail", username="omondragon", password="123")
    new_product = Products(product_name=data['product_name'], price=data['price'], origin=data['origin'])
    db.session.add(new_product)
    db.session.commit()
    return jsonify({'message': 'product created successfully'}), 201

# Update an existing user
@product_controller.route('/api/products/<int:product_id>', methods=['PUT'])
def update_user(product_id):
    print("actualizando producto")
    product = Products.query.get_or_404(product_id)
    data = request.json
    product.product_name = data['product_name']
    product.price = data['price']
    product.origin = data['origin']
    db.session.commit()
    return jsonify({'message': 'Product updated successfully'})

# Delete an existing user
@product_controller.route('/api/products/<int:product_id>', methods=['DELETE'])
def delete_user(product_id):
    product = Products.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted successfully'})
