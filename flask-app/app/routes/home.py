from flask import Blueprint, jsonify

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def index():
    return jsonify({"message": "Welcome to Flask CRUD API"})

@home_bp.route('/health')
def health():
    return jsonify({"status": "healthy"})