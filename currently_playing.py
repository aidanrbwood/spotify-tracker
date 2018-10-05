#!/usr/bin/python3

import requests
import pprint
import info_lookup

def currently_playing():
	access_token = info_lookup.access_token()
	authorization = str('Bearer ' + access_token)

	url = 'https://api.spotify.com/v1/me/player/currently-playing'
	header = { 'Authorization': authorization }
	get = requests.get(url, headers=header)

	return_object = []
	status_code = int(get.status_code)
	track_duration = 0
	track_elapsed = 0
	track = ''
	print(status_code)


	if status_code == 200:
		response = get.json()
		track_duration = response['item']['duration_ms'] / 1000
		track_elapsed = response['progress_ms'] / 1000
		album = response['item']['album']['name'].replace("-", "_")
		artist = ''
		for a in response['item']['artists']:
			artist = artist + a['name'].replace("-", "_") + ','
		artist = artist[:-1]
		song = response['item']['name'].replace("-", "_")
		track = str(song + '-' + album + '-' + artist).replace(" ", "_")
		#pprint.pprint(response)
	elif status_code == 204:
		print("nothing playing right now, or private session")
	elif status_code == 401:
		print("needs a new token")
	else:
		print("what in the fuck even happened")

	return_object.append(status_code)
	return_object.append(track_duration)
	return_object.append(track_elapsed)
	return_object.append(track)
	return return_object

def write_to_db(track):	
	database = {}
	with open('database') as d:
		for line in d:
			(identifier, playcount) = line.split()
			database[identifier] = int(playcount)

	if track in database:
		print("incrementing song...")
		database[track] = database[track] + 1;
	else:
		print("new song...")
		database[track] = 1;
		
	list_database = []
	for k in database:
		list_database.append(str(k + ' ' +  str(database[k]) + '\n'))

	with open('database', 'w') as d:
		d.writelines(list_database)
