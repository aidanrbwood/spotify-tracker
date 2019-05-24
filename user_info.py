#!/usr/bin/python3

user_folder = 'user_data'

def read_client_id():
	with open('./client_id', 'r') as f:
		id = f.read()
	return id

def read_client_secret():
	with open('./client_secret', 'r') as f:
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
	
def write_refresh_token(string):
	with open(user_folder + '/refresh_token', 'w') as f:
		f.write(string)

def write_user_id(string):
	with open(user_folder + '/client_id', 'w') as f:
		f.write(string)
	
def write_authorization_code(string):
	with open(user_folder + '/authorization_code', 'w') as f:
		f.write(string)

def write_user_secret(string):
	with open(user_folder + '/client_secret', 'w') as f:
		f.write(string)
