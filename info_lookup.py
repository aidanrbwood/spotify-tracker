#!/usr/bin/python3

def user_id():
	with open('client_id', 'r') as f:
		id = f.read()
	return id

def user_secret():
	with open('client_secret', 'r') as f:
		id = f.read()
	return id

def authorization_code():
	with open('authorization_code', 'r') as f:
		id = f.read()
	return id

def access_token():
	with open('access_token', 'r') as f:
		id = f.read()
	return id

def refresh_token():
	with open('refresh_token', 'r') as f:
		id = f.read()
	return id
