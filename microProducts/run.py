from flask import Flask, jsonify
from flask_consulate import Consul
from products.views import app


consul = Consul(app=app)

@app.route('/health')
def health():
    return jsonify({"status": "UP"}), 200

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify({"products": ["Laptop", "Mouse"]})

if __name__ == '__main__':
    consul.register_service(
        name="microProducts",
        service_id="microProducts",
        address="192.168.60.3",
        port=5003,
        tags=["flask", "products"],
        interval="10s",
        httpcheck="http://192.168.60.3:5003/health"
    )

    app.run(host="0.0.0.0", port=5003)

