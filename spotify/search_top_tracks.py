from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys
import pprint

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())




def get_artist_id(name):
    results = sp.search(q='artist:' + name, type='artist')
    id = results['artists']['items'][0]['id']
    return id


def artist_top_tracks(artist_id):
    print("This artist's top tracks:")
    response = sp.artist_top_tracks(artist_id)
    for track in response['tracks']:
        print(track['name'])


search_str = input("Which artist do you want to know?\n")
id = get_artist_id(search_str)
artist_top_tracks(id)

'''
export SPOTIPY_CLIENT_ID=fd27c40c6e2a4908be64f094bde44268
export SPOTIPY_CLIENT_SECRET=2cbdbbdfaa5247189c007626fa317040
'''
