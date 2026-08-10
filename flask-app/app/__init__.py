from flask import Flask, jsonify
from flask_restx import Api
from flask_cors import CORS

from app.models.item import db
from app.routes.items import api as items_api
from app.routes.home import home_bp

def create_app():
    app = Flask(__name__)
    
    # Configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'dev-secret-key'
    
    # Initialize extensions
    db.init_app(app)
    CORS(app)
    
    # Register home blueprint
    app.register_blueprint(home_bp)
    
    # Initialize RESTx API
    api = Api(
        app,
        version='1.0',
        title='Flask CRUD API',
        description='A simple CRUD API built with Flask',
        doc='/docs/'
    )
    
    # Register namespaces
    api.add_namespace(items_api, path='/api/items')
    
    # Create tables
    with app.app_context():
        db.create_all()
    
    return app