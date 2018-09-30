import spotipy
import spotipy.util as util

def spotify():
	client_id = "4c47d5777ede4a168dd986dd3027e9d8"
	secret = "d2dd908118c049b99d989a1c3c380b65"
	redirect_uri = "http://localhost"
	scope = "streaming"
	token = util.prompt_for_user_token('dkc52', scope, client_id, secret, redirect_uri)
	sp = spotipy.Spotify(auth=token)
	q = "artist:drake"
	result = sp.search(q)
	track = result['items'][0]['track']
	devices = sp.devices()
	sp.start_playback(devices[0], uris = [track['uri']])

