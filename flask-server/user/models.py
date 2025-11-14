from flask import Flask, jsonify

class User:
    
    def signup():
        user = {
            "_id": "",
            "name": "",
            "age": "",
            "phone": "",
            "email": ""
        } 

        return jsonify(user), 200