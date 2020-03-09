from spotipy.oauth2 import SpotifyClientCredentials
import sys
import spotipy

''' shows the albums and tracks for a given artist.
'''


def get_artist(name):
    results = sp.search(q='artist:' + name, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        return items[0]
    else:
        return None

'''
def show_album_tracks(album):
    tracks = []
    results = sp.album_tracks(album['id'])
    tracks.extend(results['items'])
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    for track in tracks:
        print('  ', track['name'])
        print()
        print(track)
'''

def artist_popular(artist):
    print('====', artist['name'], '====')
    print('Popularity: ', artist['popularity'])
    if len(artist['genres']) > 0:
        print('Genres: ', ','.join(artist['genres']))


if __name__ == '__main__':
    client_credentials_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    sp.trace = False

    name = input('please enter an artist\'s name:\n')
    artist = get_artist(name)
    print(artist)
    #artist_popular(artist)
    #show_artist_albums(artist)
    
