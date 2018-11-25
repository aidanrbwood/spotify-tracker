#!/usr/bin/python3

import requests
import pprint
import info_lookup
import spotify_logging as logging
import common_functions as cmn

def currently_playing():
	access_token = cmn.read_usr('access_token')
	authorization = str('Bearer ' + access_token)

	url = 'https://api.spotify.com/v1/me/player/currently-playing'
	header = { 'Authorization': authorization }
	get = requests.get(url, headers=header)

	return_object = []
	status_code = int(get.status_code)
	track_duration = 0
	track_elapsed = 0
	track = ''
	if status_code == 200:
		response = get.json()
		track_duration = response['item']['duration_ms'] / 1000
		track_elapsed = response['progress_ms'] / 1000
		album = response['item']['album']['name'].replace("-", "`")
		artist = ''
		for a in response['item']['artists']:
			artist = artist + a['name'].replace("-", "`") + ','
		artist = artist[:-1]
		song = response['item']['name'].replace("-", "`")
		track = str(song + '-' + album + '-' + artist).replace("_", ";").replace(" ", "_")
	elif status_code == 204:
		logging.log_verbose(str(status_code) + ": nothing playing right now, or private session")
	elif status_code == 401:
		logging.log_info(str(status_code) + ": needs a new token")
	else:
		logging.log_error(str(status_code) + ": unknown status code")

	return_object.append(status_code)
	return_object.append(track_duration)
	return_object.append(track_elapsed)
	return_object.append(track)
	return return_object

