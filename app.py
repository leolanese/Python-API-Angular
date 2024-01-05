from flask import Flask, jsonify, abort, make_response, request, render_template

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/intro', methods=['GET'])
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

@app.route('/api/tasks', methods=['GET'])
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

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': '404 - Not found'}), 404)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
