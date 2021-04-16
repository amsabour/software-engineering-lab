import json
import requests

# with open('config_file.json', 'w') as f:
#     f.write(json.dumps({'auth': 'https://localhost:9000',
#                         'user-management': 'https://localhost:8000',
#                         'profile': 'https://localhost:5000'}))

# with open('config_file.json', 'r') as f:
#     print(json.load(f))

requests.post('http://google.com', data={}, headers={'token': 'hi'})
