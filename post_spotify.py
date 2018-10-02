#!/usr/bin/python3

import requests
import base64
import info_lookup

code=info_lookup.authorization_code()
url='https://accounts.spotify.com/api/token'
redirect='http://niceme.me/'
client_id=info_lookup.user_id()
client_secret=info_lookup.user_secret()

client=str('Basic ' + client_id + ':' + client_secret)
#header={'Authorization': client}
header={'Content-Type': 'application/x-www-form-urlencoded'}

payload= (('grant_type', 'authorization_code'), ('code', code), ('redirect_uri', redirect), ('client_id', client_id), ('client_secret', client_secret))
#payload= (('grant_type', 'authorization_code'), ('code', code), ('redirect_url', redirect))
#r = requests.post(url, params=payload)
r = requests.post(url, headers=header, params=payload)
print(r.url)
print(r.status_code)
f = open("tokenfile", "w")
text = r.json()
print(text)
str1 = str(text)
f.write(str1)
f.close()
