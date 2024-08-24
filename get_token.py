import requests
from requests.auth import HTTPBasicAuth

client_id = ' '
client_secret = ' '

response = requests.post(
    'https://accounts.spotify.com/api/token',
    headers={
        'Content-Type': 'application/x-www-form-urlencoded'
    },
    data={
        'grant_type': 'client_credentials'
    },
    auth=HTTPBasicAuth(client_id, client_secret)
)


if response.status_code == 200:
    access_token = response.json()['access_token']
    print('Access Token:', access_token)
else:
    print('Failed to get access token:', response.status_code, response.text)
