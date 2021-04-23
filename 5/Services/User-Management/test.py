import requests
import jwt
import datetime
import string
import random


def create_random_user():
    signup_url = 'http://127.0.0.1:8000/add_user'
    username = ''.join(random.choices(string.ascii_lowercase, k=20))
    token = jwt.encode({'username': username, 'exp': datetime.datetime.now() + datetime.timedelta(minutes=30)}, 'MY_SECRET_KEY')

    response = requests.post(signup_url,
                             data={'username': username, 'email': 'Temp', 'mobile': 'Temp'},
                             headers={'token': token})
    print(response.text)

    return username


def get_all_users():
    token = jwt.encode({'username': 'admin', 'exp': datetime.datetime.now() + datetime.timedelta(minutes=30)}, 'MY_SECRET_KEY')
    headers = {'token': token}

    url = 'http://127.0.0.1:8000/get_all_users'

    response = requests.get(url, headers=headers, params={})
    return response.json()


create_random_user()
print(len(get_all_users()))
