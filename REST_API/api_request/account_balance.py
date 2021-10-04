import requests

url = 'http://127.0.0.1:8000/api/v1/account/balance/1'
headers = {
    'Content-Type': 'Application/json'
}

request = requests.get(url, headers=headers, )

print(request.text)
