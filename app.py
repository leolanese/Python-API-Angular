from flask import Flask, jsonify, abort, make_response, request, render_template

from flask_cors import CORS

from board import pages

app = Flask(__name__)
app.register_blueprint(pages.bp)
CORS(app)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'ERROR': '404 - Not found'}), 404)

if __name__ == '__main__':
    # Run the Flask app with CORS enabled for the entire application
    CORS(app)
    app.run(host="0.0.0.0", port=8000, debug=True)
