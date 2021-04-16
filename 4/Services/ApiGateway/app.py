from flask import Flask, abort, jsonify, request, make_response
from flask_restful import Api, Resource
import json
import requests
import jwt
import datetime

app = Flask(__name__)
api = Api(app)

service_addr = json.load('config_file.json')


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    # TODO: Check is alive

    response = requests.post(service_addr['auth'] + '/login', data={'username': username, 'password': password})
    return response


@app.route('/signup', methods=['POST'])
def signup():
    username = request.form.get('username')
    password = request.form.get('password')
    email = request.form.get('email')
    mobile = request.form.get('mobile')

    # TODO: Check is alive

    response = requests.post(service_addr['auth'] + '/signup', data={'username': username, 'password': password})

    if response.status_code != 200:
        return response

    token = response.json()['token']
    headers = {'token': token}

    response = requests.post(service_addr['profile'] + '/userprofiles', data={'username': username, 'description': "I am a new user."},
                             headers=headers)
    response = requests.post(service_addr['user-management'] + '/add_user', data={'username': username, 'email': email, 'mobile': mobile},
                             headers=headers)

    return jsonify({'message': 'User created successfully', 'token': token}), 201


@app.route('/view_profile', methods=['GET'])
def view_profile():
    username = request.form.get('username')

    # TODO: Check is alive

    response = requests.get(service_addr['profile'] + '/userprofiles/{}'.format(username))
    return response


@app.route('/edit_profile', methods=['PUT'])
def edit_profile():
    username = request.form.get('username')
    description = request.form.get('description')
    token = request.headers.get('username')

    # TODO: Check is alive

    # Verify token
    response = requests.get(service_addr['auth'] + '/is_token_valid', params={'token': token})
    if response.status_code != 200:
        return response

    response = requests.put(service_addr['profile'] + '/userprofiles/{}'.format(username), data={'description': description},
                            headers={'token': token})
    return response


if __name__ == '__main__':
    app.run(debug=True, port=10000)
