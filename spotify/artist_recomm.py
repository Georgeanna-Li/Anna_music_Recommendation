import sys
import spotipy
import pprint

''' shows recommendations for the given artist
我猜测这里应该是根据所输入的artist选取一些列相对应的recommendations
'''
from spotipy.oauth2 import SpotifyClientCredentials


client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace = False


def get_artist(name):
    results = sp.search(q='artist:' + name, type='artist')
    items = results['artists']['items']
    #选择抽取到的第一个人
    if len(items) > 0:
        return items[0]
    else:
        return None


def show_recommendations_for_artist(artist):
    results = sp.recommendations(seed_artists=[artist['id']])
    print(results['tracks'])
    artists = []
    tracks = []
    for track in results['tracks']:
        artists.append(track['name'])
        tracks.append(track['artists'][0]['name'])
    get = dict(zip(artists,tracks))
    pprint.pprint(get)
        #print(track['name'], '-', track['artists'][0]['name'])



name = input("Which artist do you want to know?\n")
artist = get_artist(name)
#print(artist)
if artist:
    show_recommendations_for_artist(artist)
else:
    print("Can't find that artist", name)
