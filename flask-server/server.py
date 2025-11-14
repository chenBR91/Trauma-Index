from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)


# Set up MongoDB connection
client = MongoClient('mongodb://localhost:27017/Demo.students')
db = client['students'] # database name
collection = db['Demo'] # mongodb://localhost:27017


# Routes

@app.route("/api", methods=['GET'])
def users():
    return jsonify({"users": ["user1", "user2"]})


if __name__ == "__main__":
    app.run(debug=True)