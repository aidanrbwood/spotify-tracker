#!/usr/bin/python3

import periodic_playing
import user_requests

menu = {}
menu['0'] = 'Exit Program'
menu['1'] = 'Start tracking'
menu['2'] = 'Stop tracking'
menu['3'] = 'Highest play track'
menu['4'] = 'Highest play artist'
menu['5'] = 'Print database'
menu['6'] = 'Print history'

options = list(menu.keys())
options.sort()

user_input = '-1'
exit_program = False
while not exit_program:
	for o in options:
		print(o + '. ' + menu[o])
	user_input = input('Please select:')
	if user_input == '0':
		periodic_playing.stop_tracking()
		exit_program = True
	elif user_input == '1':
		periodic_playing.start_tracking()
	elif user_input == '2':
		periodic_playing.stop_tracking()
	elif user_input == '3':
		user_requests.highest_play_track()
	elif user_input == '4':
		user_requests.highest_play_artist()
	elif user_input == '5':
		user_requests.print_db()
	elif user_input == '6':
		user_requests.print_history()
	else:
		print('Unknown input')	
		

