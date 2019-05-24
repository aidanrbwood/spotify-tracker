#!/usr/bin/python3

import currently_playing
import periodic_playing
import user_requests

is_tracking = False;
menu = {}
menu['0'] = 'Exit Program'
menu['1'] = 'Start tracking'
menu['2'] = 'Stop tracking'
menu['3'] = 'Highest play track'
menu['4'] = 'Highest play artist'
menu['5'] = 'Print history'

options = list(menu.keys())
options.sort()

user_input = '-1'
exit_program = False
while not exit_program:
	print('Spotify Tracker')
	print('Currently Playing: ' + currently_playing.printable_currently_playing() + "\n")
	if is_tracking:
		print('Tracking is on')
	else:
		print('Tracking is off')
	for o in options:
		print(o + '. ' + menu[o])
	user_input = input('Please select:')
	if user_input == '0':
		if is_tracking:
			print('Stopping tracking...')
			periodic_playing.stop_tracking()
		exit_program = True
	elif user_input == '1':
		if not is_tracking:
			periodic_playing.start_tracking()
			is_tracking = True
		else:
			print('Already tracking')
	elif user_input == '2':
		if not is_tracking:
			print('Not tracking')
		else:
			periodic_playing.stop_tracking()
			is_tracking = False
	elif user_input == '3':
		user_requests.highest_play_track()
	elif user_input == '4':
		user_requests.highest_play_artist()
	elif user_input == '5':
		user_requests.print_history()
	else:
		print('Unknown input')
	print('\n\n')	
		

