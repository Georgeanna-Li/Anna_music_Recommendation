from spotipy.oauth2 import SpotifyClientCredentials
import sys
import spotipy
import pprint


client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace = False

def new_relases():
    find = sp.new_releases(limit=5)
    artist_name=[]
    release=[]
    type_ =[]
    for i in range(5):
        artist_name.append(find["albums"]['items'][i]['artists'][0]['name'])
        release.append(find["albums"]['items'][i]["name"])
        type_.append(find["albums"]["items"][i]["album_type"])
    for j in range(len(artist_name)):
        print(type_[j] + "\t" + release[j] + " \t" + artist_name[j])


new_relases()




'''
export SPOTIPY_CLIENT_ID=fd27c40c6e2a4908be64f094bde44268
export SPOTIPY_CLIENT_SECRET=2cbdbbdfaa5247189c007626fa317040
'''
