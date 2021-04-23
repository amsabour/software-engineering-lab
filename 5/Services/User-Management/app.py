from flask import Flask, abort, jsonify, request, make_response
from flask_restful import Api, Resource
import jwt

app = Flask(__name__)
api = Api(app)

Users = {
    'admin': {'username': 'admin',
              'email': 'admin@example.com',
              'mobile': '090909090909',
              },
}

Profiles = {
    'admin':
        {
            'username': 'admin',
            'description': 'My lovely profile',
        }
}


def is_token_valid(token):
    if not token:
        return False, (jsonify({'message': 'Token not provided'}), 404)

    token_payload = jwt.decode(token, options={"verify_signature": False})

    if 'username' not in token_payload.keys():
        return False, (jsonify({'message': 'Token corrupted'}), 404)

    return True, token_payload['username']


@app.route('/get_all_users', methods=['GET'])
def get_all_users():
    token = request.headers.get('token')

    # Token Validation
    token_valid, response = is_token_valid(token)
    if not token_valid:
        return response
    token_username = response

    # Privilege handling
    if token_username != 'admin':
        return jsonify({'message': "You aren't allowed to access this"}), 404

    return jsonify(list(Users.values())), 200


@app.route('/get_user', methods=['GET'])
def get_user():
    username = request.args.get('username')
    token = request.headers.get('token')

    if not username:
        return jsonify({'message': 'Username not provided'}), 404

    # Token Validation
    token_valid, response = is_token_valid(token)
    if not token_valid:
        return response
    token_username = response

    # Privilege handling
    if token_username != 'admin' and token_username != username:
        return jsonify({'message': "You aren't allowed to access this"}), 404

    if username not in Users.keys():
        return jsonify({'message': 'User {} not found'.format(username)}), 404

    return jsonify(Users[username]), 200


@app.route('/add_user', methods=['POST'])
def add_user():
    username = request.form.get('username')
    email = request.form.get('email')
    mobile = request.form.get('mobile')

    if not username or not email or not mobile:
        return jsonify({'message': 'Username or email or mobile not provided'}), 404

    token = request.headers.get('token')
    # Token Validation
    token_valid, response = is_token_valid(token)
    if not token_valid:
        return response
    token_username = response

    # Privilege handling
    if token_username != username:
        return jsonify({'message': "Tried creating an account with mismatched token"}), 404

    if username in Users:
        return jsonify({'message': 'User {} already exists'.format(username)}), 404

    Users[username] = {
        'username': username,
        'email': email,
        'mobile': mobile,
    }

    Profiles[username] = {
        'username': username,
        'description': ''
    }

    return jsonify(Users[username]), 200


@app.route('/profiles/<username>', methods=['GET'])
def get_profile(username):
    if username not in Profiles.keys():
        return jsonify({'message': 'User {} not found'.format(username)}), 404

    return jsonify(Profiles[username]), 200


@app.route('/profiles/<username>', methods=['PUT'])
def update_profile(username):
    description = request.json.get('description')
    token = request.headers.get('token')

    if description is None:
        return jsonify({'message': 'New description not provided'}), 404

    # Token Validation
    token_valid, response = is_token_valid(token)
    if not token_valid:
        return response
    token_username = response

    # Privilege handling
    if token_username != username:
        return jsonify({'message': "You may not edit others profiles"}), 404

    if username not in Profiles.keys():
        return jsonify({'message': 'User {} not found'.format(username)}), 404

    Profiles[username]['description'] = description
    return Profiles[username]


@app.route('/is_alive', methods=['GET'])
def is_alive():
    return jsonify({'message': 'Service is alive'}), 200


if __name__ == '__main__':
    app.run(debug=True, port=8000)
