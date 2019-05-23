#!/usr/bin/python3

import requests
import user_info

client_id = user_info.read_user_id()

payload = (('client_id', client_id), ('response_type', 'code'), ('redirect_uri', 'http://niceme.me/'), ('scope', 'user-read-currently-playing'))
r = requests.get('https://accounts.spotify.com/authorize/', params=payload)
print(r.url)
print(r.status_code)
