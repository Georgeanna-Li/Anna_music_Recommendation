from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys


client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def related_artist(artist_name):
    result = sp.search(q='artist:' + artist_name, type='artist')
    name = result['artists']['items'][0]['name']
    uri = result['artists']['items'][0]['uri']
    related = sp.artist_related_artists(uri)
    print('Related artists for', name)
    for artist in related['artists']:
        print('  ', artist['name'])


artist_name = input('who do you want to know?\n')
related_artist(artist_name)