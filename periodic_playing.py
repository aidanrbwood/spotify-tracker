#!/usr/bin/python3

import currently_playing
import refresh
import threading

previous_track_id = ''
previous_play_time = 0

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
					currently_playing.write_to_db(track_id)
		else:
			currently_playing.write_to_db(track_id)
			previous_track_id = track_id
		previous_play_time = play_time
			

def timer_shell():
	threading.Timer(10.0, timer_shell).start()
	track_logic()
	print("called logic")

timer_shell()

