#!/usr/bin/python3

import database_helper

def highest_play_track():
	db = database_helper.open_db()
	highest_play = []
	for (track, plays) in db.items():
		if highest_play == []:
			highest_play.append(track) 
		elif plays > db[highest_play[0]]:
			highest_play = []
			highest_play.append(track)
		elif plays == db[highest_play[0]]:
			highest_play.append(track)
	print("The highest play tracks are: ")
	for track in highest_play:
		database_helper.print_track(track, db[track])

def print_db():
	db = database_helper.open_db()
	for (track, plays) in db.items():
		database_helper.print_track(track, plays)

	
