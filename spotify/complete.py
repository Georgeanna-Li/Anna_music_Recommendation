import random
import re
from rasa.nlu import config
from rasa.nlu.model import Trainer
from rasa.nlu.config import RasaNLUModelConfig
from rasa.nlu.training_data import load_data
import spacy
import spotipy
import pprint
import sys
from spotipy.oauth2 import SpotifyClientCredentials

# Get spotify credentials
client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace = False

# Load en_core_web_md from spacy (used to extract entities)
nlp = spacy.load("en_core_web_md")

# Create a trainer that uses this config
trainer = Trainer(config.load("config_spacy.yml"))

# Load the training data
training_data = load_data('rasa.json')

# Create an interpreter by training the model
interpreter = trainer.train(training_data)

# Further interpret the message and decides its intent
def interpret(message):
    msg = message.lower()
    process = interpreter.parse(msg)
    intent = process['intent']['name']
    return intent

def get_artist_id(name):
    results = sp.search(q=name, type='artist')
    id = results['artists']['items'][0]['id']
    return id


def get_album_id(name):
    results = sp.search(q=name, type='album')
    id = results['albums']['items'][0]['id']
    return id


#  Input an album name，return its album_id, artist_id
def get_album_artist(search_str):
    results = sp.search(q='album:' + search_str, type='album', limit=5)
    artist_id = results['albums']['items'][0]['artists'][0]['id']
    artist_name = results['albums']['items'][0]['artists'][0]['name']
    album_id = results['albums']['items'][0]['id']
    release_date = results['albums']['items'][0]['release_date']
    return album_id, artist_id


#  Input album_id, and return album tracks
def show_album_tracks(album_id):
    tracks = []
    results = sp.album_tracks(album_id)
    tracks.extend(results['items'])
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    for track in tracks:
        print('  ', track['name'])


# Given a genre, return a playlistname, playlist_id(needs to be combined with playlist_tracks)
def genre_search(genre):
    find = sp.category_playlists(category_id=genre, limit=2)
    if find:
        listname = find["playlists"]["items"][0]["name"]
        list_id = find["playlists"]["items"][0]["id"]
        return list_id
    else:
        return "none"


# Playlist tracks, needs list_id as input
def playlist_tracks(list_id):
    find = sp.playlist_tracks(playlist_id=list_id, limit=15)
    music = []
    artist = []
    for i in range(6):
        music.append(find["items"][i]["track"]["name"])
        artist.append(find["items"][i]["track"]["artists"][0]["name"])
    for j in range(len(music)):
        print(artist[j] + ": \t" + music[j])


# Print the recommendations of tracks and their artists based on an aritst
def recommendations_for_artist(artist_id):
    results = sp.recommendations(seed_artists=[artist_id], limit=20)
    artists = []
    tracks = []
    for track in results['tracks']:
        artists.append(track['name'])
        tracks.append(track['artists'][0]['name'])
    for i in range(5):
        print(tracks[i] + ":\t" + artists[i])


# Recommend artists based on a given artist
def related_artist(artist_name):
    result = sp.search(q=artist_name, type='artist', limit=5)
    name = result['artists']['items'][0]['name']
    uri = result['artists']['items'][0]['uri']
    related = sp.artist_related_artists(uri)
    print('Related artists for', name)
    for artist in related['artists']:
        print('  ', artist['name'])


# give new releases and their types(single/album)
def new_releases():
    find = sp.new_releases(limit=5)
    artist_name = []
    release = []
    type_ = []
    for i in range(5):
        artist_name.append(find["albums"]['items'][i]['artists'][0]['name'])
        release.append(find["albums"]['items'][i]["name"])
        type_.append(find["albums"]["items"][i]["album_type"])
    print("These are the latest releases:\n")
    for j in range(len(artist_name)):
        print(type_[j] + "\t" + release[j] + " \t" + artist_name[j])

# If the user demands more new releases:
def new_releases_more():
    find = sp.new_releases(limit=5, offset=5)
    artist_name = []
    release = []
    type_ = []
    for i in range(5):
        artist_name.append(find["albums"]['items'][i]['artists'][0]['name'])
        release.append(find["albums"]['items'][i]["name"])
        type_.append(find["albums"]["items"][i]["album_type"])
    print("These are the latest releases:\n")
    for j in range(len(artist_name)):
        print(type_[j] + "\t" + release[j] + " \t" + artist_name[j])

# The top ten tracks for the given artist: (no limits set)
def artist_top_tracks(artist_id):
    print("This artist's top tracks:")
    response = sp.artist_top_tracks(artist_id)
    for track in response['tracks']:
        print(track['name'])



genre = ['toplists', 'pop', 'hiphop', 'chill', 'kpop', 'mood', 'rock',
         'sleep', 'rnb', 'focus', 'jazz', 'workout', 'classical', 'romance', 'party', 'inspirational',
         'soul', 'wellness', 'travel', 'family', 'dinner', 'latin',
         'gaming', 'country', 'funk', 'punk', 'metal', 'blues']


if __name__ == '__main__':
    client_credentials_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    user_id = input("Hi! Please input your user_id:\n")
    message = input("Let's begin! What do you wanna know?\n")
    intent = interpret(message)
    if intent == "greet":
        print("HEY THERE! I am your music bot~")
        print(
            "Try to get your recommendations by typing an artist, an album or a music genre you like.")
        message = input()
        intent = interpret(message)
    match = re.search("(.*)what(.*)", message)
    if match is not None:
        print("You can start by typing artist/album + name")

    while intent != "goodbye":
        if intent == "latest":
            new_releases()
            rectify = input()
            if "more" in rectify:
                new_releases_more()
            message = input()
            intent = interpret(message)

        if intent == "artist_search" or " by " in message:
            print("It seems that you love the artist. Can you retype his/her name?")  # Further ensure that the user is requiring artist_search
            entity = input()
            b1 = get_artist_id(entity)
            b2 = artist_top_tracks(b1)
            us = input("Wanna see other similar artists?\n")
            if interpret(us) == 'affirm':
                print("Here's what I find:")
                b3 = related_artist(entity)
                us2 = input(
                    "I can recommend other tracks if you like " + entity + "!\n")
                if interpret(us2) == "affirm":
                    b4 = recommendations_for_artist(b1)
            print("OK, what else?")

        if intent == "music_search" or "album" in message:
            match = re.search("(.*)album(.+)", message)  # use regular expression to get the album name
            if match is None:
                name = input(
                    "Are you looking for an album? If so, please tell me its full name:\n")
            else:
                name = match.group(2)
            a1 = get_album_id(name)
            print("For album : " + name + " I have found its tracks for you")
            a2 = show_album_tracks(a1)
            intent = "none"

        if intent == "genre_search":
            doc = nlp(message)
            entity = "default"
            for i in range(len(doc)):
                if doc[i].text in genre:
                    entity = doc[i].text
            if entity == "default":
                entity = random.choice(genre)
                print(
                    "I am sorry-there seems to be no such genre,\n let me give you the " + entity + " instead:")
            c1 = genre_search(entity)
            print("Here is a playlist of " + entity)
            c2 = playlist_tracks(c1)
        message = input()
        intent = interpret(message)
    print("It is nice to help you! Have a good day!")
