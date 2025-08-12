from flask import jsonify
from flask_consulate import Consul
from web.views import app  # ya tienes la app aquí

consul = Consul(app=app)

@app.route('/health')
def health():
    return jsonify({"status": "UP"}), 200

if __name__ == '__main__':
    consul.register_service(
        name="frontend",
        service_id="frontend",
        address="192.168.60.3",
        port=5001,
        tags=["flask", "frontend"],
        interval="10s",
        httpcheck="http://192.168.60.3:5001/health"
    )

    app.run(host="0.0.0.0", port=5001)

