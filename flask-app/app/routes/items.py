from flask import Blueprint, request, jsonify
from flask_restx import Namespace, Resource, fields

from app.models.item import db, Item
from app.schemas.item import item_schema, items_schema

# Flask Blueprint
items_bp = Blueprint('items', __name__)

# Flask-RESTx Namespace (for Swagger docs)
api = Namespace('items', description='Item operations')

# Define model for Swagger
item_model = api.model('Item', {
    'name': fields.String(required=True, description='Item name'),
    'description': fields.String(description='Item description'),
    'price': fields.Float(required=True, description='Item price')
})

@api.route('/')
class ItemList(Resource):
    @api.doc('get_items')
    def get(self):
        """Get all items"""
        items = Item.query.all()
        return jsonify(items_schema.dump(items))
    
    @api.doc('create_item')
    @api.expect(item_model)
    def post(self):
        """Create a new item"""
        data = request.get_json()
        
        # Validate required fields
        if not data.get('name'):
            return {'error': 'Name is required'}, 400
        if not data.get('price'):
            return {'error': 'Price is required'}, 400
            
        new_item = Item(
            name=data['name'],
            description=data.get('description'),
            price=data['price']
        )
        db.session.add(new_item)
        db.session.commit()
        return jsonify(item_schema.dump(new_item)), 201

@api.route('/<int:item_id>')
class ItemResource(Resource):
    @api.doc('get_item')
    def get(self, item_id):
        """Get item by ID"""
        item = Item.query.get(item_id)
        if not item:
            return {'error': 'Item not found'}, 404
        return jsonify(item_schema.dump(item))
    
    @api.doc('update_item')
    @api.expect(item_model)
    def put(self, item_id):
        """Update an item"""
        item = Item.query.get(item_id)
        if not item:
            return {'error': 'Item not found'}, 404
            
        data = request.get_json()
        if 'name' in data:
            item.name = data['name']
        if 'description' in data:
            item.description = data['description']
        if 'price' in data:
            item.price = data['price']
            
        db.session.commit()
        return jsonify(item_schema.dump(item))
    
    @api.doc('delete_item')
    def delete(self, item_id):
        """Delete an item"""
        item = Item.query.get(item_id)
        if not item:
            return {'error': 'Item not found'}, 404
            
        db.session.delete(item)
        db.session.commit()
        return '', 204

# Register blueprint (will be used in app/__init__.py)
def register_routes(app):
    app.register_blueprint(items_bp, url_prefix='/api/items')