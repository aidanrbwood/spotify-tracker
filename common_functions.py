#!/usr/bin/python3

import os.path

#Folders
USR = './user_data'
DATA = './databases'

#USER INFO FILES
AUTH_CODE = 'authorization_code'
ACCESS_TOKEN = 'access_token'
CLIENT_ID	= 'client_id'
CLIENT_SECRET = 'client_secret'
REFRESH_TOKEN = 'refresh_token'

#DATA FILES
LIBRARY = 'library'
HISTORY = 'history'

def check_files():
	folders = [usr, data]
	user_files = [AUTH_CODE, ACCESS_TOKEN, CLIENT_ID, CLIENT_SECRET, REFRESH_TOKEN]
	data_files = [LIBRARY, HISTORY]

	for folder in folders:
		if not os.path.isdir(folder):
			os.mkdir(folder)

	for f in user_files:
		if not os.path.isfile(usr + '/' + f):
			open(usr + '/' + f, '+w')

	for f in data_files:
		if not os.path.isfile(data + '/' + f):
			open(data + '/' + f, '+w')

