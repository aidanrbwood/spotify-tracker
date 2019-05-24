#!/usr/bin/python3

import sqlite3
from sqlite3 import Error
import datetime 
import database_helper as printer

DB_PATH = "./databases/music.db"

def open_connection():
	try:
		connection = sqlite3.connect(DB_PATH)
	except Error as e:
		print(e)
	return connection

def close_connection(connection):
	try:
		connection.close()
	except Error as e:
		print(e)
	

def create_tables():
	connection = open_connection()
	crsr = connection.cursor()
	
	command = """CREATE TABLE IF NOT EXISTS songs (
	TrackID varchar(255) NOT NULL,
	Artist varchar(255) NOT NULL,
	Album varchar(255) NOT NULL,
	Name varchar(255) NOT NULL,
	TrackNumber int NOT NULL,
	Plays int NOT NULL,
	MostRecentPlay datetime NOT NULL,
	PRIMARY KEY (TrackID)
	);"""

	crsr.execute(command)
	
	command = """CREATE TABLE IF NOT EXISTS artists (
	ArtistID varchar(255) NOT NULL,
	Artist varchar(255) NOT NULL,
	Plays int NOT NULL,
	PRIMARY KEY (ArtistID)
	);"""
	
	crsr.execute(command)
	connection.commit()
	close_connection(connection)

def check_song_existence(track_id):
	connection = open_connection()
	crsr = connection.cursor()

	command = """SELECT * FROM songs WHERE TrackID='""" + track_id + """'"""
	crsr.execute(command)
	song = crsr.fetchall()
	close_connection(connection)
	return song

def check_artist_existence(artist_id):
	connection = open_connection()
	crsr = connection.cursor()

	command = """SELECT * FROM artists WHERE ArtistID='""" + artist_id + """'"""
	crsr.execute(command)
	artist = crsr.fetchall()
	close_connection(connection)
	return artist

def fetch_song_plays(track_id):
	connection = open_connection()
	crsr = connection.cursor()

	command = """SELECT Plays FROM songs WHERE TrackID='""" + track_id + """'"""
	crsr.execute(command)
	plays = crsr.fetchall()
	close_connection(connection)
	return plays[0][0]

def fetch_artist_plays(artist_id):
	connection = open_connection()
	crsr = connection.cursor()

	command = """SELECT Plays FROM artists WHERE ArtistID='""" + artist_id + """'"""
	crsr.execute(command)
	plays = crsr.fetchall()
	close_connection(connection)
	return plays[0][0]

def current_song(track):
	#print(track)
	song_exists = check_song_existence(track['track_id'])
	artist_exists = check_artist_existence(track['artist_id'])
	if not song_exists:
		add_song(track)
	else:
		increment_song(track['track_id'])

	if not artist_exists:
		add_artist(track)
	else:
		increment_artist(track['artist_id'])
		
		
def increment_song(track_id):
	connection = open_connection()
	crsr = connection.cursor()
	command = """UPDATE songs
	SET Plays = ?,
			MostRecentPlay = ?
	WHERE TrackID = ?"""
	tup = [fetch_song_plays(track_id) + 1, datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'), track_id]
	crsr.execute(command, tup)
	connection.commit()
	close_connection(connection)

def increment_artist(artist_id):
	connection = open_connection()
	crsr = connection.cursor()
	command = """UPDATE artists
	SET Plays = ?
	WHERE ArtistID = ?"""
	tup = [fetch_artist_plays(artist_id) + 1, artist_id]
	crsr.execute(command, tup)
	connection.commit()
	close_connection(connection)

def add_artist(artist):
	connection = open_connection()
	crsr = connection.cursor()
	artist_arr = []
	artist_arr.append(artist['artist_id'])
	artist_arr.append(artist['artist'])
	artist_arr.append("1")

	command = """INSERT INTO artists(ArtistID, Artist, Plays)
	VALUES(?,?,?)"""
	crsr.execute(command, artist_arr)
	connection.commit()
	close_connection(connection)

def add_song(track):
	connection = open_connection()
	crsr = connection.cursor()
	track_arr = []
	track_arr.append(track['track_id'])
	track_arr.append(track['artist'])
	track_arr.append(track['album'])
	track_arr.append(track['name'])
	track_arr.append(track['track_number'])
	track_arr.append("1")
	track_arr.append(datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'))

	command = """INSERT INTO songs(TrackID, Artist, Album, Name, TrackNumber, Plays, MostRecentPlay)
	VALUES(?,?,?,?,?,?,?)"""
	crsr.execute(command,track_arr)
	connection.commit()
	close_connection(connection)

def add_test_song(num):
	track = {}
	track['track_id'] = str(num)
	track['artist'] = "ARTIST"
	track['album'] = "ALBUM"
	track['name'] = "NAME"
	track['track_number'] = 1
	track['artist_id'] = "ARTIST_ID"
	current_song(track)

def add_test_artist():
	artist = {}
	artist['artist'] = "ARTIST"
	artist['artist_id'] = "ARTISTID"
	add_artist(artist)


def print_most_played_artist():
	connection = open_connection()
	connection = open_connection()
	crsr = connection.cursor()

	command = """SELECT * FROM artists ORDER BY Plays DESC"""
	crsr.execute(command)
	song = crsr.fetchall()
	close_connection(connection)
	
	header = {}
	header['artist'] = "ARTIST"
	header['plays'] = "PLAYS"
	printer.print_artist(header)
	for result in song:
		printer.print_artist(convert_artist(result))

def print_most_played_song():
	connection = open_connection()
	connection = open_connection()
	crsr = connection.cursor()

	command = """SELECT * FROM songs ORDER BY Plays DESC"""
	crsr.execute(command)
	song = crsr.fetchall()
	close_connection(connection)

	header = {}
	header['name'] = "NAME"
	header['album'] = "ALBUM"
	header['plays'] = "PLAYS"
	header['artist'] = "ARTIST"
	printer.print_track(header)
	for result in song:
		printer.print_track(convert_track(result))

def print_history():
	connection = open_connection()
	connection = open_connection()
	crsr = connection.cursor()

	command = """SELECT * FROM songs ORDER BY MostRecentPlay DESC"""
	crsr.execute(command)
	song = crsr.fetchall()
	close_connection(connection)

	header = {}
	header['name'] = "NAME"
	header['album'] = "ALBUM"
	header['plays'] = "PLAYS"
	header['artist'] = "ARTIST"
	printer.print_track(header)
	for result in song:
		printer.print_track(convert_track(result))

def convert_artist(artist):
#('ARTIST_ID', 'ARTIST', 3)
	d_artist = {}
	d_artist['artist_id'] = artist[0]
	d_artist['artist'] = artist[1]
	d_artist['plays'] = artist[2]
	return d_artist

def convert_track(track):
#('TRACK_ID', 'ARTIST', 'ALBUM', 'NAME', 1, 2, '2019-05-23 20:46:08')
	d_track = {}
	d_track['track_id'] = track[0]
	d_track['artist'] = track[1]
	d_track['album'] = track[2]
	d_track['name'] = track[3]
	d_track['track_num'] = track[4]
	d_track['plays'] = track[5]
	d_track['played_at'] = track[6]
	return d_track
