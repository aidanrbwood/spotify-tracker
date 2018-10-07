#!/usr/bash/python3

import unicodedata
import spotify_logging as logging

def open_db():
	database = {}
	with open('database') as d:
		for line in d:
			(identifier, playcount) = line.split()
			database[identifier] = int(playcount)
	return database

def print_track(track, plays):
	fields = track.split('-')
	song = fields[0]
	album = fields[1]
	artist = fields[2]
	filler = "                                        "
	if (len(song) + wide_chars(song[:37]) > 37):
		song = song[:37 - wide_chars(song[:37])] + '...'
	else:
		song = song + filler[:40-len(song)-wide_chars(song)]
	if (len(album) + wide_chars(album[:37]) > 37):
		album = album[:37 - wide_chars(album[:37])] + '...'
	else:
		album = album + filler[:40-len(album)-wide_chars(album)]
	if (len(artist) + wide_chars(artist[:37]) > 37):
		artist = artist[:37 - wide_chars(artist[:37])] + '...'
	else:
		artist = artist + filler[:40-len(artist)-wide_chars(artist)]
		
	print(song + ' ' + album + ' ' + artist + ' ' + str(plays))

def print_artist(artist, plays):
	filler = "                                        "

	if (len(artist) + wide_chars(artist[:37]) > 37):
		artist = artist[:37 - wide_chars(artist[:37])] + '...'
	else:
		artist = artist + filler[:40-len(artist)-wide_chars(artist)]
	print(artist + ' ' + str(plays))
	
	
def write_to_db(track):	
	database = {}
	with open('database') as d:
		for line in d:
			(identifier, playcount) = line.split()
			database[identifier] = int(playcount)

	if track in database:
		logging.log_info("incrementing song " + track)
		database[track] = database[track] + 1;
	else:
		logging.log_info("new song " + track)
		database[track] = 1;
		
	list_database = []
	for k in database:
		list_database.append(str(k + ' ' +  str(database[k]) + '\n'))

	with open('database', 'w') as d:
		d.writelines(list_database)

def wide_chars(s):
    return sum(unicodedata.east_asian_width(x)=='W' for x in s)
