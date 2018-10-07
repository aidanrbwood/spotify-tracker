#!/usr/bin/python3

import datetime

def log_info(msg):
	with open('spotify.log', 'a') as log:
		log.write('INFO:\t' + current_time() + '\t' + msg + '\n')

def log_error(msg):
	with open('spotify.log', 'a') as log:
		log.write('ERROR:\t'+ current_time() + '\t' + msg + '\n')

def current_time():
	return str(datetime.datetime.utcnow()).split('.')[0]

	
