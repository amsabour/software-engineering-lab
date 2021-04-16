from flask import Flask, abort, jsonify, request, make_response
from flask_restful import Api, Resource
import json
import requests
from requests.exceptions import Timeout
import datetime
import jwt
import datetime

app = Flask(__name__)
api = Api(app)

with open("C:\\Users\\Asus\\Desktop\\AZ Software Engineering\\4\\Services\\ApiGateway\\config_file.json", 'r') as f:
    service_addr = json.load(f)

service_strikes = {x: (0, 0) for x in service_addr.keys()}


def flaskify_response(response):
    return response.content, response.status_code, response.headers.items()


def check_service_alive(service):
    strikes, timestamp = service_strikes[service]
    if strikes >= 3 and datetime.datetime.now().timestamp() < timestamp:
        return False
    elif strikes >= 3 and datetime.datetime.now().timestamp() >= timestamp:
        service_strikes[service] = (0, datetime.datetime.now().timestamp())

    try:
        response = requests.get(service_addr[service] + '/is_alive')
        if response.status_code == 200:
            service_strikes[service] = (0, datetime.datetime.now().timestamp())
            return True
    except Timeout:
        pass

    strikes, _ = service_strikes[service]
    service_strikes[service] = (strikes + 1, (datetime.datetime.now() + datetime.timedelta(seconds=30)).timestamp())


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if not check_service_alive('auth'):
        return jsonify({'message': 'Internal server error'}), 500

    response = requests.post(service_addr['auth'] + '/login', data={'username': username, 'password': password})
    return flaskify_response(response)


@app.route('/signup', methods=['POST'])
def signup():
    username = request.form.get('username')
    password = request.form.get('password')
    email = request.form.get('email')
    mobile = request.form.get('mobile')

    if not check_service_alive('auth') or not check_service_alive('profile') or not check_service_alive('user-management'):
        return jsonify({'message': 'Internal server error'}), 500

    response = requests.post(service_addr['auth'] + '/signup', data={'username': username, 'password': password})

    if response.status_code != 200:
        return flaskify_response(response)

    token = response.json()['token']
    headers = {'token': token}

    response = requests.post(service_addr['profile'] + '/userprofiles',
                             json={'username': username, 'description': "I am a new user."},
                             headers=headers)
    response = requests.post(service_addr['user-management'] + '/add_user',
                             data={'username': username, 'email': email, 'mobile': mobile},
                             headers=headers)

    return jsonify({'message': 'User created successfully', 'token': token}), 201


@app.route('/view_profile', methods=['GET'])
def view_profile():
    username = request.args.get('username')

    if not check_service_alive('profile'):
        return jsonify({'message': 'Internal server error'}), 500

    response = requests.get(service_addr['profile'] + '/userprofiles/{}'.format(username))
    return flaskify_response(response)


@app.route('/edit_profile', methods=['PUT'])
def edit_profile():
    username = request.form.get('username')
    description = request.form.get('description')
    token = request.headers.get('token')

    if not check_service_alive('auth') or not check_service_alive('profile'):
        return jsonify({'message': 'Internal server error'}), 500

    # Verify token
    response = requests.get(service_addr['auth'] + '/is_token_valid', params={'token': token})
    if response.status_code != 200:
        return flaskify_response(response)

    response = requests.put(service_addr['profile'] + '/userprofiles/{}'.format(username),
                            json={'description': description},
                            headers={'token': token})
    return flaskify_response(response)


if __name__ == '__main__':
    app.run(debug=True, port=10000)
