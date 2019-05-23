#!/usr/bin/python3

import database_helper
import db_access as db

def highest_play_track():
	db.print_most_played_song()

def highest_play_artist():
	db = database_helper.open_db()
	artist_plays = {}
	for (track, plays) in db.items():
		artist = track.split('-')[2]
		if not artist in artist_plays:
			artist_plays[artist] = plays
		else:
			artist_plays[artist] = artist_plays[artist] + plays
	highest_play = []
	for (artist, plays) in artist_plays.items():
		if highest_play == []:
			highest_play.append(artist)
		elif plays > artist_plays[highest_play[0]]:
			highest_play = []
			highest_play.append(artist)
		elif plays == artist_plays[highest_play[0]]:
			highest_play.append(artist)
	print("The highest play arists are: ")
	for artist in highest_play:
		database_helper.print_artist(artist, artist_plays[artist])
				
def print_history():
	db.print_history()
