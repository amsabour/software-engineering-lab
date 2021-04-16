import requests

url = 'http://localhost:10000/signup'
data = {'username': 'user5', 'password': 'password', 'email': 'abcd@example.com', 'mobile': '12321321123'}

response = requests.post(url, data=data)
print(response.status_code)
print(response.text)
