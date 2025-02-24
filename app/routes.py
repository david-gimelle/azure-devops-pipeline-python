from app import app
from flask import jsonify

@app.route('/ping', methods=['GET'])
def pinging():
    return jsonify({"message": "pong"}), 200

@app.route('/demo', methods=['GET'])
def get_demo():
    return jsonify({"message": "demo"}), 200

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"}), 200
