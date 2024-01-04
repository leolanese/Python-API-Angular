from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/intro')
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

if __name__ == '__main__':
    app.run(debug=True)
