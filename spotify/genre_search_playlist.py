from spotipy.oauth2 import SpotifyClientCredentials
import sys
import spotipy
import pprint


client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace = False

def genre_search(genre):
    find = sp.category_playlists(category_id=genre, limit=2)
    if find:
        listname = find["playlists"]["items"][0]["name"]
        list_id = find["playlists"]["items"][0]["id"]
        return list_id
    else:
        return "none"


def playlist_tracks(list_id):
    find = sp.playlist_tracks(playlist_id=list_id,limit=25)
    music=[]
    artist=[]
    for i in range(20):
        music.append(find["items"][i]["track"]["name"])
        artist.append(find["items"][i]["track"]["artists"][0]["name"])
    for j in range(len(music)):
        print(music[j] + " \tby artist: " + artist[j])


name = input('input genre type:\n')
id = genre_search(name)
print(playlist_tracks(id))




#results = sp.search(q='playlist:' + name, type='playlist', limit=1)
#pprint.pprint(results)




'''
export SPOTIPY_CLIENT_ID=fd27c40c6e2a4908be64f094bde44268
export SPOTIPY_CLIENT_SECRET=2cbdbbdfaa5247189c007626fa317040
'''
