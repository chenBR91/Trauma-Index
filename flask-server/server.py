from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from user.models import User

app = Flask(__name__)
CORS(app)


# Set up MongoDB connection
try:
    client = MongoClient('localhost', 27017)  # mongodb://localhost:27017
    db = client['Demo'] # this is the database
    collection = db['students'] # this is the collection
except:
    print('Error - Cannot connect to db')


# Routes

@app.route('/user/signup', methods=['GET'])
def signup():
    return User.signup()


@app.route("/add_user", methods=['POST']) 
def add_user():
    collection.insert_one({'name': 'Alex', 'age': 30, 'phone': '8888', 'email': 'email'})
    all_studets = collection.find()
    return jsonify({'users': 'fd'})


@app.route("/", methods=['GET'])
def get_all_users():
    all_users = collection.find()
    print(f'users {all_users}')
    return jsonify({'users': 'fd'})

@app.route("/api", methods=['GET'])
def users():
    return jsonify({"users": ["user1", "user2"]})


if __name__ == "__main__":
    app.run(debug=True)