import requests

url = 'http://localhost:10000/signup'
data = {'username': 'usdd', 'password': 'password', 'email': 'abcd@example.com', 'mobile': '12321321123'}

response = requests.post(url, data=data)
print(response.status_code)
print(response.text)


data = {'username': data["username"], 'password': 'password'}
response = requests.post('http://localhost:10000/login', data=data)
print(response.text)

token = response.json()['token']

url = 'http://localhost:10000/edit_profile'
headers = {'token': token}
data = {'username': data["username"], 'description': 'THIS IS MY ASDLKASDASLDKASDLK'}

response = requests.put(url, data=data, headers=headers)
print(response.status_code)
print(response.text)
