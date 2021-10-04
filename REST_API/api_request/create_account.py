import json

import requests

url = 'http://127.0.0.1:8000/api/v1/account/account/'
headers = {
    'Content-Type': 'Application/json'
}
data = {
    'name': 'Demo',
    'number': '10000000001000000100',
    'overdraft': False,
    'balance': 1000000
}
request = requests.post(url, headers=headers, data=json.dumps(data))

print(request.text)
