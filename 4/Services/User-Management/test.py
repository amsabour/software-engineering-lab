import requests

login_data = {'username': 'admin',
              'password': 'password'}

login_url = 'http://127.0.0.1:8000/login'

response = requests.post(login_url, data=login_data)

token = response.json()['token']
headers = {'token': token}

data = {'username': 'admin'}
url = 'http://127.0.0.1:9000/get_user'

response = requests.get(url, headers=headers, params=data)
print(response.text)


