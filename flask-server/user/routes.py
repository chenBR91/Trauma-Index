from flask import Flask
from user.models import User

app = Flask(__name__)

@app.route('/user/signup', methods=['GET'])
def signup():
    return User.signup()

