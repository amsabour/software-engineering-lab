from flask import Flask, abort, jsonify, request, make_response
from flask_selfdoc import Autodoc
import jwt

app = Flask(__name__)
auto = Autodoc(app)

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
@auto.doc()
def get_all_users():
    """
    [ADMIN ONLY]
    Return a list of all users.
    """
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
@auto.doc()
def get_user():
    """
    Get the information of a user.
    Works only if admin or token matches username.
    """
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
@auto.doc()
def add_user():
    """
    Add a new user to the database.
    Works only if token matches username.
    """

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
@auto.doc()
def get_profile(username):
    """
    Get profile of a user.
    """
    if username not in Profiles.keys():
        return jsonify({'message': 'User {} not found'.format(username)}), 404

    return jsonify(Profiles[username]), 200


@app.route('/profiles/<username>', methods=['PUT'])
@auto.doc()
def update_profile(username):
    """
    Update profile of a user.
    Works only if token matches username.
    """

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
@auto.doc()
def is_alive():
    """
    Health check for service.
    Returns status code 200 on success. Else, does not return anything (This should be used with a timeout).
    """
    return jsonify({'message': 'Service is alive'}), 200


@app.route('/documentation')
def documentation():
    return auto.html()


if __name__ == '__main__':
    app.run(debug=True, port=8000)
