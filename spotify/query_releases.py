import spacy
import spotipy
import pprint
import sys
from spotipy.oauth2 import SpotifyClientCredentials
import re
import sqlite3
import random

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace = False


def new_releases():
    find = sp.new_releases(limit=40)
    artist_name = []
    release = []
    type_ = []
    for i in range(40):
        artist_name.append(find["albums"]['items'][i]['artists'][0]['name'])
        release.append(find["albums"]['items'][i]["name"])
        type_.append(find["albums"]["items"][i]["album_type"])
    return artist_name, release, type_

# create the table new_releases
conn = sqlite3.connect('new_releases.db')
c = conn.cursor()
c.execute("DROP TABLE IF EXISTS new_releases")
c.execute("CREATE TABLE IF NOT EXISTS new_releases (artist_name, release, type_)")

# insert value into the table
artist_name, release, type_ = new_releases()
for i in range(len(artist_name)):
    table = (artist_name[i], release[i], type_[i])
    c.execute(
        "INSERT INTO new_releases(artist_name, release, type_) VALUES (?, ?, ?)", table)
    c.execute("commit")

responses = [
    '{} is a top hit!',
    'I would recommend {} for you!',
    '{} is one option for you, but I know more than that :)'
    'How about {}?'
    'Try {} and tell me if you like it!'
    'I am wondering if you would like this: {}'
    'I think {} fits your requirement~'
]


def what_type_only(choice):
    a = c.execute(
        "SELECT release from new_releases WHERE type_ = ? ", (choice,))
    # tuples in a list[('Never Worn White',), ('Gaslighter',), ('SKYBOX',), ...]
    k = a.fetchall()
    result = [r[0] for r in k]
    if result:
        print(random.choice(responses).format(result[1]))
    else: print("sorrrrrrrrry")


def artist_only(choice):
    a = c.execute(
        "SELECT release from new_releases WHERE artist_name LIKE ?",
        (choice+"%",))
    result = [r[0] for r in a.fetchall()]
    if result:
        print(random.choice(responses).format(result[0]))
    else: print("Sorrrry")



print("Hi, here are 100 latest releases for you to choose:")
msg1 = input("Do you like album or single?")
what_type_only(msg1)
msg2 = input("Which artist do you like?")
artist_only(msg2)

'''
a = c.execute("SELECT type_,artist_name FROM new_releases WHERE artist_name like ?",('L%',))
print(a.fetchall())
'''



'''
export SPOTIPY_CLIENT_ID=fd27c40c6e2a4908be64f094bde44268
export SPOTIPY_CLIENT_SECRET=2cbdbbdfaa5247189c007626fa317040
'''
