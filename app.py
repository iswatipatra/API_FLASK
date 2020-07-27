from flask import Flask, request, jsonify
import re

app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
    username = request.json['username']
    password = request.json['password']

    pattern = re.compile("^(?=.*[a-zA-Z])(?=.*[0-9])")

    if username.isalpha():
        if pattern.match(password):
            if len(password) == 6:
                status = 200
                msg = 'Success'
            else:
                status = 201
                msg = 'Failure: password should be of length 6'
        else:
            status = 202
            msg = 'Failure: password to have 1 character and 1 number'
    else:
        status = 203
        msg = 'Failure: only characters allowed in username'

    return jsonify(status=status, msg=msg)


