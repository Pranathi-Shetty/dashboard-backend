from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Fake database (temporary)
users = {
    "admin": "1234"
}

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username in users and users[username] == password:
        return jsonify({"message": "Login successful", "token": "fake-jwt-token"}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401

@app.route("/progress", methods=["GET"])
def get_progress():
    return jsonify({"progress": 40, "water": 5})

if __name__ == "__main__":
    app.run(debug=True)
