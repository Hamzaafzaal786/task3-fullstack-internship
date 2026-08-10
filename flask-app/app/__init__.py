from flask import Flask, jsonify

def create_app():
    app = Flask(__name__)
    
    @app.route('/')
    def index():
        return jsonify({"message": "Welcome to Flask CRUD API"})
    
    @app.route('/health')
    def health():
        return jsonify({"status": "healthy"})
    
    return app