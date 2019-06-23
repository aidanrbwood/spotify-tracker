#!/usr/bin/python3

import datetime

ENABLED = False
verbose = False

def log_info(msg):
	global ENABLED
	if enabled:
		with open('spotify.log', 'a') as log:
			log.write('INFO:\t' + current_time() + '\t' + msg + '\n')

def log_error(msg):
	global ENABLED
	if enabled:
		with open('spotify.log', 'a') as log:
			log.write('ERROR:\t'+ current_time() + '\t' + msg + '\n')

def current_time():
    return datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

def log_verbose(msg):
    global verbose
    if verbose:    
        with open('spotify.log', 'a') as log:
            log.write('INFO:\t' + current_time() + '\t' + msg + '\n')
