#!/usr/bin/python3

import requests
import pprint
import user_info
import spotify_logging as logging

def currently_playing():
	access_token = user_info.read_access_token()
	authorization = str('Bearer ' + access_token)

	url = 'https://api.spotify.com/v1/me/player/currently-playing'
	header = { 'Authorization': authorization }
	get = requests.get(url, headers=header)

	return_object = {}
	status_code = int(get.status_code)
	track_duration = 0
	track_elapsed = 0
	track = {}
	if status_code == 200:
		response = get.json()
		#print(response)
		track_duration = response['item']['duration_ms'] / 1000
		track_elapsed = response['progress_ms'] / 1000
		album = response['item']['album']['name']
		track_num = response['item']['track_number']
		track_id = response['item']['id']
		song = response['item']['name']
		artist = ''
		artist_id = ''
		for a in response['item']['artists']:
			artist = artist + a['name'] + ', '
			artist_id = artist_id + a['id'] + ','
		artist = artist[:-2]
		artist_id = artist_id[:-1]

		track['track_number'] = track_num
		track['track_id'] = track_id
		track['name'] = song
		track['album'] = album
		track['artist'] = artist
		track['artist_id'] = artist_id
		#print("track:\n")	
		#print(track)

	elif status_code == 204:
		logging.log_verbose(str(status_code) + ": nothing playing right now, or private session")
	elif status_code == 401:
		logging.log_info(str(status_code) + ": needs a new token")
	else:
		logging.log_error(str(status_code) + ": unknown status code")

	return_object['status_code'] = status_code
	return_object['track_duration'] = track_duration
	return_object['track_elapsed'] = track_elapsed
	return_object['track'] = track
	return return_object

