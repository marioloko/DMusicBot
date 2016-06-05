from apiclient.discovery import build
import argparse
import json
import requests
import spotipy
import os

"""
	DMusicBot.py is intended to be a lib for Telegram's DMusicBot
	with the respectives search and download methods.

	The searchers and downloader methods are a modification of the
	Spotify-Downloader(https://github.com/akul08/Spotify-Downloader)
	code, modified in order to fit better to the telegram Bot.
"""
# File that contains bot's help data
HELP_FILE = 'help.txt'

# Advertisement track if no track_name
ADVERTISEMENT = os.environ['ADVERTISEMENT']

# Youtube API keys
DEVELOPER_KEY = os.environ['YOUTUBEKEY']
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

# Only one global spotify instantie (for avoiding useless wastes of memory)
sp = spotipy.Spotify()

# Only one global youtube instantie (for avoiding useless wastes of memory)
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
	developerKey=DEVELOPER_KEY)

def search(track_name):
	"""
		search: print the youtube url of track_name
			track_name: name of the track we are looking for
	"""
	return youtube_watch( youtube_search( spotify_search(track_name) ) )

def download(track_name):
	"""
		download: print the download url of track_name
			track_name: name of the track we are looking for
	"""
	return youtube_download( youtube_search( spotify_search(track_name) ) )

def usearch(track_name):
	"""
		usearch: print the youtube url of track_name
				(does not check in spotify if it is a song)
			track_name: name of the track we are looking for
	"""
	return youtube_watch( youtube_search(track_name) )

def udownload(track_name):
	"""
		udownload: print the download url of track_name
				(does not check in spotify if it is a song)
			track_name: name of the track we are looking for
	"""
	return youtube_download( youtube_search(track_name) )

def help():
	"""
		help: get the help of how to use the bot store in HELP_FILE
	"""
	with open(HELP_FILE) as f:
		content = f.read()
	return content

def spotify_search(track_name):
	"""
		spotify_search: search in spotify for a song and its artist
			track_name: name of the track we are searching for
			return: artist name + track name
	"""
	if not track_name:
		track_name = ADVERTISEMENT

	results = sp.search(q=track_name, limit=1, type='track')
	tracks = results['tracks']['items']

	for track in tracks:
		return "%32.32s %s" % (track['artists'][0]['name'], track['name'])

def youtube_search(track_name):
	"""
		youtube_search: search in youtube for the videoId of a track
			track_name: name of the track we are searching for
			return: track's videoId
	"""
	if not track_name:
		track_name = ADVERTISEMENT

	results = youtube.search().list(
		q=track_name,
		part="id,snippet",
		maxResults=1,
		).execute()

	for video in results['items']:
		video_id = video['id']
		if video_id['kind'] == 'youtube#video':
			return video_id['videoId']

def youtube_download(video_id):
	"""
		youtube_download: get the download link for a youtube video
			video_id: video identifyer in youtube
			return: url for downloading the video
	"""
	link = 'http://youtubeinmp3.com/fetch/?format=JSON&video=http://www.youtube.com/watch?v=%s' % video_id
	r = requests.get(link)
	try:
		data = json.loads(r.text)
		download_link = data['link']

	except ValueError:
		from bs4 import BeautifulSoup as bs
		soup = bs(r.text, 'html.parser')
		download = soup.find(id='download')
		if not download:
			return 'Track not found for downloading'
		download_link = 'http://www.youtubeinmp3.com/download/%s' % download['href']

	return download_link

def youtube_watch(video_id):
	"""
		youtube_watch: get the url for wathc that video_id
			video_id: video identifyer in youtube
			return: url for watch the video
	"""
	return 'https://www.youtube.com/watch?v=%s' % video_id


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('track', 
		help='Name of the track we are looking for', 
		type=str) 
	parser.add_argument('--search', 
		dest='search', 
		help='Search for a music youtube video', 
		action='store_true') 
	parser.add_argument('--download', 
		dest='download', 
		help='Download a music youtube video in mp3',action='store_true') 
	parser.add_argument('--usearch', 
		dest='usearch', 
		help='Unsecure search for a youtube video(it is not granted that the video is musical) faster',
		action='store_true') 
	parser.add_argument('--udownload', dest='udownload', 
		help='Unsecure download a youtube video in mp3(it is not granted that the video is musical) faster',
		action='store_true') 

	args = parser.parse_args()

	if (args.search):
		print search(args.track)
	elif (args.download):
		print download(args.track)
	elif (args.usearch):
		print usearch(args.track)
	elif (args.udownload):
		print udownload(args.track)

if __name__ == '__main__':
	main()
