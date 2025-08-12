from users.views import app
from flask import Flask, jsonify
from flask_consulate import Consul


consul = Consul(app=app)

@app.route('/health')
def health():
    return jsonify({"status": "UP"}), 200

@app.route('/users', methods=['GET'])
def get_products():
    return jsonify({"users": ["Juan", "Maria"]})

if __name__ == '__main__':
    consul.register_service(
        name="microUsers",
        service_id="microUsers",
        address="192.168.60.3",
        port=5002,
        tags=["flask", "users"],
        interval="10s",
        httpcheck="http://192.168.60.3:5002/health"
    )

    app.run(host="0.0.0.0", port=5002)
