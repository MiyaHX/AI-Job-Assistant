from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'message': 'AI Job Assistant API is running'
    }), 200

@app.route('/api/info', methods=['GET'])
def get_info():
    return jsonify({
        'name': 'AI Job Assistant',
        'version': '1.0.0'
    }), 200

if __name__ == '__main__':
    app.run(debug=True, port=5001)
