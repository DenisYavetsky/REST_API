import datetime
import json

import requests

url = 'http://127.0.0.1:8000/api/v1/account/transfer/'
headers = {
    'Content-Type': 'Application/json'
}

data = {
    'operation_dt': datetime.datetime.now().__str__(),
    'account_from': 2,
    'account_to': 2,
    'cost': 100
}
request = requests.post(url, headers=headers, data=json.dumps(data))

print(request.text)
