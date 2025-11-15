from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient

from user.models import User

app = Flask(__name__)
CORS(app)  # Prevent the cors error


# Set up MongoDB connection
try:
    client = MongoClient('localhost', 27017)  # mongodb://localhost:27017
    db = client['Demo'] # this is the database
    collection = db['students'] # this is the collection
    collectionUser = db['user']
except:
    print('Error - Cannot connect to db')


# Routes

@app.route('/user/signup', methods=['GET'])
def signup():
    return User.signup()


@app.route("/add_user", methods=['POST']) 
def add_user():
    collection.insert_one({'name': 'Alex', 'age': 30, 'phone': '8888', 'email': 'email'})
    return jsonify({'users': 'fd'})


@app.route("/", methods=['POST', 'GET'])
def get_all_users():
    if request.method == 'GET':
        allUsers = collection.find()
        usersJson = []
        for user in allUsers:
            name = user['name']
            age = user['age']
            phone = user['phone']
            email = user['email']
            id = user['_id']

            userDict = {
                "id": str(id),
                "name": str(name),
                "age": int(age),
                "phone": str(phone),
                "email": str(email)
            }

            usersJson.append(userDict)
            

    return jsonify({'users': usersJson})


@app.route("/api", methods=['GET'])
def users():
    return jsonify({"users": ["user1", "user2"]})


# API users only once
import requests
@app.route("/api/read/data/only-once", methods=['GET'])
def readData():
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    data = response.json()
    print(data)

    users = []
    for user in data:
        completed = user['completed']
        id = user['id']
        title = user['title']
        userId = user['userId']

        userJson = {
            'completed': completed,
            'id': id,
            'title': title,
            'userId': userId
        }

        users.append(userJson)

    collectionUser.insert_many(users)
    return jsonify({"user": data})



if __name__ == "__main__":
    app.run(debug=True)