from flask import Flask, Blueprint, jsonify

# Create a Blueprint pages
bp = Blueprint("pages", __name__)

# intro view
@bp.route('/api/intro', methods=['GET'])
def intro():
    data = {
        'message': 'Python server API message',
        'status': 'success',
        'data': {
            'key1': 'value1',
            'key2': 'value2'
        }
    }
    return jsonify(data)

# home view
@bp.route("/")
def home():
    return "API Server root - http://localhost:8000/"

# tasks view
@bp.route('/api/tasks', methods=['GET'])
def get_tasks():
    data = [
        {
            'id': 1,
            'title': u'Buy groceries',
            'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
            'done': False
        },
        {
            'id': 2,
            'title': u'Learn Python',
            'description': u'Need to find a good Python tutorial on the web',
            'done': False
        }
    ]
    return jsonify(data)