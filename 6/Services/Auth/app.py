from flask import Flask, abort, jsonify, request, make_response
from flask_selfdoc import Autodoc
import jwt
import datetime

app = Flask(__name__)
auto = Autodoc(app)
app.config['SECRET_KEY'] = 'MY_SECRET_KEY'

Users = {
    'admin': {'username': 'admin',
              'password': 'password'},
}


@app.route('/login', methods=['POST'])
@auto.doc()
def login():
    """
    Login user with username and password.
    Returns json with token if successful.
    """
    username = request.form.get('username')
    password = request.form.get('password')
    print(username, password)

    if not username or not password:
        return jsonify({'message': 'Username or password not provided'}), 404

    if username not in Users.keys():
        return jsonify({'message': 'User {} not found'.format(username)}), 404

    if Users[username]['password'] != password:
        return jsonify({'message': 'Username or password is incorrect'}), 404

    token = jwt.encode({'username': username, 'exp': datetime.datetime.now() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
    return jsonify({'token': token}), 200


@app.route('/signup', methods=['POST'])
@auto.doc()
def signup():
    """
    Signup user with username and password.
    Returns json with token if successful.
    """
    username = request.form.get('username')
    password = request.form.get('password')

    if not username or not password:
        return jsonify({'message': 'Username or password not provided'}), 404

    if username in Users:
        return jsonify({'message': 'User {} already exists'.format(username)}), 404

    Users[username] = {'username': username, 'password': password}
    token = jwt.encode({'username': username, 'exp': (datetime.datetime.now() + datetime.timedelta(minutes=30)).timestamp()},
                       app.config['SECRET_KEY'])
    return jsonify({'token': token}), 200


@app.route('/is_token_valid', methods=['GET'])
@auto.doc()
def is_token_valid():
    """
    Check if token is valid and hasn't been tampered with.
    Returns status code 200 if okay and status code 403 if not.
    """
    token = request.args.get('token')
    print(token, not token)

    if not token:
        return jsonify({'message': 'Token is missing!'}), 403

    try:
        print(token, app.config['SECRET_KEY'])
        data = jwt.decode(token, app.config['SECRET_KEY'], algorithms='HS256')

        if data["exp"] < datetime.datetime.now().timestamp():
            return jsonify({'message': 'Token has expired'}), 403

        return jsonify({'message': 'Token is valid'}), 200
    except Exception as e:
        print(e)
        return jsonify({'message': 'Token is invalid'}), 403


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
    app.run(debug=True, port=9000)
