#!/usr/bin/python3

import currently_playing
import refresh
import threading
import spotify_logging as logging
import db_access as db

# These three variables need to be static
previous_track_id = ''
previous_play_time = 0
tracking = False

#########################################################################
# track_logic
# inputs: 
#		None
#	outputs: 
#		None
# side effects:
#		if the correct conditions are met it will pass song and artist
#		data to db_access for writing into the databases
# purpose: 
# 	decides whether the currently playing track has been playing
# 	enough and isn't the same play of the same song to register as a play 
# 	if it is, pass it off to db_access to get added/incremented in the db
#########################################################################
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
		#print(r)
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
			
#######################################################################
# timer_shell
# inputs: 
#		None
#	outputs: 
#		None
# side effects:
#		recursively calls itself every 10 seconds if track is on to spawn a 
#		new thread that then runs track_logic
# purpose: 
#		implements the periodic nature of the tracker, when tracking is on
#		the first call to the function spawns a timed thread that runs
#		timer_shell again after a 60s delay, and then it runs track_logic
#		this creates a cycle of every 10s a new thread running track_logic
#		so that the current spotify data is consistently analyzed
#		I had the value at 10s previously, and you can change it if you want
#		but I was having a problem with maxing out the # of API calls you
#		can make in a certain amount of time
#######################################################################
def timer_shell():
    global tracking
    if tracking:	
    	threading.Timer(60.0, timer_shell).start()
    	track_logic()

#########################################################################
# stop_tracking
# inputs: 
#		None
#	outputs:
#		None
# side effects:
#		sets tracking to false and logs
# purpose:
#		wraps the act of setting the tracking global to false for use
#		by other functions such as user_requests
#########################################################################
def stop_tracking():
    global tracking
    tracking = False
    logging.log_info('Stopping tracking...')

#########################################################################
#	start_tracking 
# inputs: 
#		None
#	outputs: 
#		None
# side effects:
#		sets tracking to true and logs
# purpose: 
#		wraps the act of settings the tracking global to true for use by 
#		other functions such as user_requests
#########################################################################
def start_tracking():
    global tracking
    logging.log_info('Starting tracking...')
    tracking = True
    timer_shell()
