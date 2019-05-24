#!/usr/bin/python3

import database_helper
import db_access as db

def highest_play_track():
	db.print_most_played_song()

def highest_play_artist():
	db.print_most_played_artist()
				
def print_history():
	db.print_history()

def delete_dbs():
	db.empty_tables()

