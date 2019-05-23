#!/usr/bin/python3

import currently_playing
import refresh
import threading
import spotify_logging as logging
import database_helper
import db_access as db

previous_track_id = ''
previous_play_time = 0
tracking = False

def track_logic():
	global previous_track_id
	global previous_play_time
	r = currently_playing.currently_playing()
	response_code = r['status_code']
	if response_code == 401:
		refresh.refresh_token()
		r = currently_playing.currently_playing()
		response_code = r['status_code']
	if response_code == 200:
		print(r)
		track_time = r['track_duration']
		play_time = r['track_elapsed']
		track_id = r['track']['track_id']
		if previous_track_id == track_id:
			if play_time < previous_play_time:
				elapsed = previous_play_time - play_time
				if elapsed > 80:
					db.current_song(r['track'])
				previous_play_time = play_time
		elif play_time >= 20:
					db.current_song(r['track'])
					previous_track_id = track_id
					previous_play_time = play_time
		else:
				logging.log_verbose("new track_id, but has not been played long enough to register as a play, waiting until 20+ seconds to play")
			
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
