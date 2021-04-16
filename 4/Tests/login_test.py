import requests

url = 'http://localhost:10000/login'
data = {'username': 'admin', 'password': 'password'}

response = requests.post(url, data=data)
print(response.status_code)
print(response.text)
