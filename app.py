from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Flask API работает!"})

@app.route('/ping')
def ping():
    return jsonify({"status": "ok", "ping": "pong"})

if name == '__main__':
    app.run(debug=True)
