from flask import Flask, abort, jsonify, request, make_response
from flask_selfdoc import Autodoc

import json
import requests
from requests.exceptions import Timeout

import datetime
import jwt

app = Flask(__name__)
auto = Autodoc(app)

with open("./config_file.json", 'r') as f:
    service_addr = json.load(f)

service_strikes = {x: (0, 0) for x in service_addr.keys()}


def flaskify_response(response):
    return response.content, response.status_code, response.headers.items()


def check_service_alive(service):
    strikes, timestamp = service_strikes[service]
    if strikes >= 3 and datetime.datetime.now().timestamp() < timestamp:
        print("Service {} is down ---- Letting it rest for now".format(service))
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
    print("Service {} is down".format(service))
    return False


@app.route('/login', methods=['POST'])
@auto.doc()
def login():
    """
    Login user with username and password.
    Returns json with token if successful.
    """
    username = request.form.get('username')
    password = request.form.get('password')

    if not check_service_alive('auth'):
        return jsonify({'message': 'Internal server error'}), 500

    response = requests.post(service_addr['auth'] + '/login', data={'username': username, 'password': password})
    return flaskify_response(response)


@app.route('/signup', methods=['POST'])
@auto.doc()
def signup():
    """
    Signup user with username and password.
    Returns json with username, email, and mobile if successful.
    """
    username = request.form.get('username')
    password = request.form.get('password')
    email = request.form.get('email')
    mobile = request.form.get('mobile')

    if not check_service_alive('auth') or not check_service_alive('user-management'):
        return jsonify({'message': 'Internal server error'}), 500

    response = requests.post(service_addr['auth'] + '/signup', data={'username': username, 'password': password})

    if response.status_code != 200:
        return flaskify_response(response)

    token = response.json()['token']
    headers = {'token': token}

    response = requests.post(service_addr['user-management'] + '/add_user',
                             data={'username': username, 'email': email, 'mobile': mobile},
                             headers=headers)

    return flaskify_response(response)


@app.route('/view_profile', methods=['GET'])
@auto.doc()
def view_profile():
    """
    Get profile of a user.
    Token not needed.
    """
    username = request.args.get('username')

    if not check_service_alive('user-management'):
        return jsonify({'message': 'Internal server error'}), 500

    response = requests.get(service_addr['user-management'] + '/profiles/{}'.format(username))
    return flaskify_response(response)


@app.route('/edit_profile', methods=['PUT'])
@auto.doc()
def edit_profile():
    """
    Update profile of a user.
    Works only if token matches username.
    """

    username = request.form.get('username')
    description = request.form.get('description')
    token = request.headers.get('token')

    if not check_service_alive('auth') or not check_service_alive('user-management'):
        return jsonify({'message': 'Internal server error'}), 500

    # Verify token
    response = requests.get(service_addr['auth'] + '/is_token_valid', params={'token': token})
    if response.status_code != 200:
        return flaskify_response(response)

    response = requests.put(service_addr['user-management'] + '/profiles/{}'.format(username),
                            json={'description': description},
                            headers={'token': token})
    return flaskify_response(response)


@app.route('/get_all_users', methods=['GET'])
@auto.doc()
def get_all_users():
    """
    Gets the list of all users.
    Works only if token matches admin token.
    """
    print("Im here")
    token = request.headers.get('token')

    if not check_service_alive('auth') or not check_service_alive('user-management'):
        return jsonify({'message': 'Internal server error'}), 500

    # Verify token
    response = requests.get(service_addr['auth'] + '/is_token_valid', params={'token': token})
    if response.status_code != 200:
        return flaskify_response(response)

    response = requests.get(service_addr['user-management'] + '/get_all_users',
                            headers={'token': token})

    return flaskify_response(response)


@app.route('/book', methods=['POST'])
@auto.doc()
def create_book():
    """
    Create a new book.
    Works only if token matches admin token.
    """

    title = request.form.get('title')
    category = request.form.get('category')
    author = request.form.get('author')
    token = request.headers.get('token')

    if not check_service_alive('auth') or not check_service_alive('books'):
        return jsonify({'message': 'Internal server error'}), 500

    # Verify token
    response = requests.get(service_addr['auth'] + '/is_token_valid', params={'token': token})
    if response.status_code != 200:
        return flaskify_response(response)

    response = requests.post(service_addr['books'] + '/books',
                             json={'title': title, 'author': author, 'category': category},
                             headers={'token': token})

    return flaskify_response(response)


@app.route('/book/<book_id>', methods=['GET'])
@auto.doc()
def read_book(book_id):
    """
    Get info of book by id.
    """

    if not check_service_alive('books'):
        return jsonify({'message': 'Internal server error'}), 500

    response = requests.get(service_addr['books'] + '/books/{}'.format(book_id))
    return flaskify_response(response)


@app.route('/book/<book_id>', methods=['PUT'])
@auto.doc()
def update_book(book_id):
    """
    Update book information.
    Works only if token matches admin token.
    """

    title = request.form.get('title')
    category = request.form.get('category')
    author = request.form.get('author')
    token = request.headers.get('token')

    if not check_service_alive('auth') or not check_service_alive('books'):
        return jsonify({'message': 'Internal server error'}), 500

    # Verify token
    response = requests.get(service_addr['auth'] + '/is_token_valid', params={'token': token})
    if response.status_code != 200:
        return flaskify_response(response)

    response = requests.put(service_addr['books'] + '/books/{}'.format(book_id),
                            json={'title': title, 'author': author, 'category': category},
                            headers={'token': token})

    return flaskify_response(response)


@app.route('/book/<book_id>', methods=['DELETE'])
@auto.doc()
def delete_book(book_id):
    """
    Delete a book by id.
    Works only if token matches admin token.
    """

    token = request.headers.get('token')

    if not check_service_alive('auth') or not check_service_alive('books'):
        return jsonify({'message': 'Internal server error'}), 500

    # Verify token
    response = requests.get(service_addr['auth'] + '/is_token_valid', params={'token': token})
    if response.status_code != 200:
        return flaskify_response(response)

    response = requests.delete(service_addr['books'] + '/books/{}'.format(book_id),
                               headers={'token': token})

    return flaskify_response(response)


@app.route('/book/search', methods=['GET'])
@auto.doc()
def search_books():
    """
    Searches books by title and category.
    A book is returned if matches the given category (if provided) and contains the title string provided in book title.
    """
    title = request.args.get('title', None)
    category = request.args.get('category', None)

    if not check_service_alive('books'):
        return jsonify({'message': 'Internal server error'}), 500

    response = requests.post(service_addr['books'] + '/search',
                             json={'title': title, 'category': category})
    return flaskify_response(response)


@app.route('/documentation')
def documentation():
    return auto.html()


if __name__ == '__main__':
    app.run(debug=True, port=10000)
