from flask import Flask, abort, jsonify, request, make_response
from flask_restful import Api, Resource
import jwt

app = Flask(__name__)
api = Api(app)

Users = {
    'admin': {'username': 'admin',
              'email': 'admin@example.com',
              'mobile': '090909090909'},
}


def verify_token(token, username):
    if not token:
        return False, (jsonify({'message': 'Token not provided'}), 404)

    token_payload = jwt.decode(token, options={"verify_signature": False})

    if 'username' not in token_payload.keys():
        return False, (jsonify({'message': 'Token corrupted'}), 404)

    if username != token_payload['username']:
        return False, (jsonify({'message': 'Token is invalid'}), 404)

    return True, None


@app.route('/get_user', methods=['GET'])
def get_user():
    username = request.args.get('username')
    token = request.headers.get('token')

    if not username:
        return jsonify({'message': 'Username not provided'}), 404

    is_token_valid, response = verify_token(token, username)
    if not is_token_valid:
        return response

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
    is_token_valid, response = verify_token(token, username)
    if not is_token_valid:
        return response

    if username in Users:
        return jsonify({'message': 'User {} already exists'.format(username)}), 404

    Users[username] = {'username': username, 'email': email, 'mobile': mobile}
    return jsonify(Users[username]), 200


@app.route('/is_alive', methods=['GET'])
def is_alive():
    return jsonify({'message': 'Service is alive'}), 200


if __name__ == '__main__':
    app.run(debug=True, port=8000)
