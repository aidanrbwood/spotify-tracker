#!/usr/bin/python3

user_folder = 'user_data'

def read_user_id():
	with open(user_folder + '/client_id', 'r') as f:
		id = f.read()
	return id

def read_user_secret():
	with open(user_folder + '/client_secret', 'r') as f:
		id = f.read()
	return id

def read_authorization_code():
	with open(user_folder + '/authorization_code', 'r') as f:
		id = f.read()
	return id

def read_access_token():
	with open(user_folder + '/access_token', 'r') as f:
		id = f.read()
	return id

def read_refresh_token():
	with open(user_folder +'/refresh_token', 'r') as f:
		id = f.read()
	return id

def write_access_token(string):
	with open(user_folder + '/access_token', 'w') as f:
		f.write(string)
	return 0
