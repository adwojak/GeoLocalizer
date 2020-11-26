from requests import post

register = 'http://localhost:8000/register/'
token = 'http://localhost:8000/token/'
fetch_address = 'http://localhost:8000/fetch-address/'
headers = {'Content-type': 'application/json'}
username = {"username": "username", "password": "password"}
addresses = ['www.google.com', 'www.facebook.com', 'www.gmail.com', 'www.youtube.com', 'www.mcdonalds.com']

post(register, headers=headers, json=username)
access_token = post(token, headers=headers, json=username).json()['access']
jwt_headers = headers.copy()
jwt_headers['Authorization'] = 'Bearer {0}'.format(access_token)

for address in addresses:
    post(fetch_address, headers=jwt_headers, json={"address": address})
