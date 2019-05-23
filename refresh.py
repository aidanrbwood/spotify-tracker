#!/usr/bin/python3

import requests
import base64
import subprocess
import user_info
import spotify_logging as logging

def refresh_token():
	refresh_token = user_info.read_refresh_token()
	url = 'https://accounts.spotify.com/api/token'
	client_id = 'def3e457b3604f958efa7a419bb277bf'
	client_secret = 'a244c4f6748c498c896be0f18f918700'

	client = str(client_id + ':' + client_secret)
	encoded = str(base64.b64encode(bytes(client, 'utf-8')))[2:-1]
	bb = str('Basic ' + encoded)

	header = {'Authorization': bb, 'Content-Type': 'application/x-www-form-urlencoded'}
	payload = (('grant_type', 'refresh_token'), ('refresh_token', refresh_token))

	r = requests.post(url, headers=header, params=payload)
	logging.log_info('refresh code status code ' + str(r.status_code))
	response = r.json()
	returned_token = response['access_token']
	user_info.write_access_token(returned_token)
