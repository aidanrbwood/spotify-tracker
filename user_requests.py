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

def print_db():
	db = database_helper.open_db()
	artists = {}
	for track in db:
		elements = track.split('-')
		if elements[2] in artists:
			if elements[1] in artists[elements[2]]:
				artists[elements[2]][elements[1]][elements[0]] = track
			else:
				artists[elements[2]][elements[1]] = {}
				artists[elements[2]][elements[1]][elements[0]] = track
		else:
			artists[elements[2]] = {}
			artists[elements[2]][elements[1]] = {}
			artists[elements[2]][elements[1]][elements[0]] = track
	artist_list = list(artists.keys())
	artist_list.sort()
	for artist in artist_list:
		album_list = list(artists[artist].keys())
		album_list.sort()
		for album in album_list:
			song_list = list(artists[artist][album].keys())
			song_list.sort()
			for song in song_list:
				database_helper.print_track(artists[artist][album][song], db[artists[artist][album][song]])
				
def print_history():
	history = database_helper.open_history()
	for track in history:
		database_helper.print_track(track, '')		
