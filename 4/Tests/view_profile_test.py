import requests

url = 'http://localhost:10000/view_profile'
data = {'username': 'user1'}

response = requests.get(url, params=data)
print(response.status_code)
print(response.text)
