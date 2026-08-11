from celery import Celery
from flask import Flask, jsonify
import time

# Create Celery instance
def make_celery(app_name=__name__):
    return Celery(
        app_name,
        broker='redis://localhost:6379/0',
        backend='redis://localhost:6379/0'
    )

celery = make_celery()

@celery.task
def process_data(data):
    """Background task"""
    print(f"Processing: {data}")
    time.sleep(5)  # Simulate long processing
    print(f"Completed: {data}")
    return f"Processed {data}"

# Flask App
app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"message": "Flask Celery Demo"})

@app.route('/process/<int:item_id>')
def process_item(item_id):
    # Submit task to Celery
    task = process_data.delay({"item": item_id})
    return jsonify({"task_id": task.id, "status": "Processing in background"})

if __name__ == '__main__':
    app.run(port=5001, debug=True)