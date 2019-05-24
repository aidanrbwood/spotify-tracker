#!/usr/bin/python3

import requests
import user_info
import common_functions
import base64
import db_access

common_functions.check_files()
db_access.create_tables()

client_id = user_info.read_user_id()
payload = (('client_id', client_id), ('response_type', 'code'), ('redirect_uri', 'http://niceme.me/'), ('scope', 'user-read-currently-playing'))
r = requests.get('https://accounts.spotify.com/authorize/', params=payload)
print("Copy and paste the following URL into your browser, once you have done so login and you will be redirected, when you are redirected copy the URL enter it into the following prompt")
print(r.url)
redirect_url = input("Redirect URL: ")
auth_code = redirect_url.split('code=')[1]
user_info.write_authorization_code(auth_code)

client_secret = user_info.read_user_secret()
url='https://accounts.spotify.com/api/token'
redirect='http://niceme.me/'


client=str('Basic ' + client_id + ':' + client_secret)
header={'Content-Type': 'application/x-www-form-urlencoded'}

payload= (('grant_type', 'authorization_code'), ('code', auth_code), ('redirect_uri', redirect), ('client_id', client_id), ('client_secret', client_secret))
r = requests.post(url, headers=header, params=payload)
resp = r.json()

access_token = resp['access_token']
refresh_token = resp['refresh_token']

user_info.write_access_token(access_token)
user_info.write_refresh_token(refresh_token)

print("You have successly complete the setup process for the Spotify Tracker, run the user_interface file to access the application and happy listening!")
