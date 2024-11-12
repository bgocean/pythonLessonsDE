import requests
import json

# Set up the URL
url = 'http://45.135.233.242:8001/to_insert'

# Set up the headers
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer your_token'
}

# Set up the request body
payload = {
    # 'username': 'berd@digitalberd.com',
    # 'password': '123'
    'symbol': '125'
}

json_payload = json.dumps(payload)

# Make the POST request
response = requests.post(url=url, params=payload)
print(response)
# Check the response
if response.status_code == 200:
    print('Request successfully')
    print(response.json())
else:
    print('Request failed')
    print(response.text)
