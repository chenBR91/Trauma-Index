from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Routes

@app.route("/api", methods=['GET'])
def users():
    return jsonify({"users": ["user1", "user2"]})


if __name__ == "__main__":
    app.run(debug=True)