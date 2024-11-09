import requests
import json

from samba.dcerpc.dcerpc import payload, response

# Set up the URL
url = 'https://robotfastapi.digitalberd.com/auth/login'

# Set up the headers
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer your_token'
}

# Set up the request body
payload = {
    'username': 'berd@digitalberd.com',
    'password': 123
}

json_payload = json.dumps(payload)

# Make the POST request
response = requests.post(url, headers=headers, data=json_payload)
print(response)
# Check the response
if response.status_code == 200:
    print('Request successfully')
    print(response.json())
else:
    print('Request failed')
    print(response.text)
