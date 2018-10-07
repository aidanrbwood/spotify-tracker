#!/usr/bash/python3

def open_db():
	database = {}
	with open('database') as d:
		for line in d:
			(identifier, playcount) = line.split()
			database[identifier] = int(playcount)
	return database

def print_track(track, plays):
	fields = track.split('-')
	print(fields[0] + '\t' + fields[1] + '\t' + fields[2] + '\t' + str(plays))
	
