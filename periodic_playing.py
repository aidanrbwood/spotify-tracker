#!/usr/bin/python3

import currently_playing
import refresh
import threading
import spotify_logging as logging
import database_helper

previous_track_id = ''
previous_play_time = 0
tracking = True

def track_logic():
	global previous_track_id
	global previous_play_time

	r = currently_playing.currently_playing()
	response_code = r[0]
	if response_code == 401:
		refresh.refresh_token()
		r = currently_playing.currently_playing()
		response_code = r[0]
	if response_code == 200:
		track_time = r[1]
		play_time = r[2] 
		track_id = r[3]
		if previous_track_id == track_id:
			if play_time < previous_play_time:
				elapsed = previous_play_time - play_time
				if elapsed > 80:
					database_helper.write_to_db(track_id)
					database_helper.add_to_history(track_id)
		else:
			database_helper.write_to_db(track_id)
			database_helper.add_to_history(track_id)
			previous_track_id = track_id
		previous_play_time = play_time
			

def timer_shell():
	global tracking
	if tracking:	
		threading.Timer(10.0, timer_shell).start()
		track_logic()

def stop_tracking():
	global tracking
	tracking = False
	logging.log_info('Stopping tracking...')

def start_tracking():
	global tracking
	logging.log_info('Starting tracking...')
	tracking = True
	timer_shell()
