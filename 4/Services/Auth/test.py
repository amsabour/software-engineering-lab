import requests

data = {'username': 'admin',
        'password': 'password'}

url = 'http://127.0.0.1:5000/login'

response = requests.post(url, data=data)
print(response.text)

