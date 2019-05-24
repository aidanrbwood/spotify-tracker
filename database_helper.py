#!/usr/bash/python3

import unicodedata
import spotify_logging as logging

def print_track(track):
	song = track['name']
	album = track['album']
	artist = track['artist']
	plays = track['plays']
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

def print_artist(input_artist):
	artist = input_artist['artist']
	plays = input_artist['plays']
	filler = "                                        "

	if (len(artist) + wide_chars(artist[:37]) > 37):
		artist = artist[:37 - wide_chars(artist[:37])] + '...'
	else:
		artist = artist + filler[:40-len(artist)-wide_chars(artist)]
	print(artist + ' ' + str(plays))


def wide_chars(s):
    return sum(unicodedata.east_asian_width(x)=='W' for x in s)
