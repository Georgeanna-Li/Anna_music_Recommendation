# Anna_music_Recommendation
A project for NLP, a chatbot linked to Facebook fan page to recommend music based on users' requirements

# PURPOSE
Recently I began learning about NLP, and here is a chatbot I built to recommend music.
Since I am a total green hand on this, I first build a bot that I can talk to on my Mac terminal, then I linked it with a FB fan page I created to intilize my bot.
There are a number of changes commited when I am transplanting my python code to the Messenger bot, so I will upload two versions of code. For orinal python code, see the file spotify_github.py; for latter version, see webhook.py.

Since I am learning NLP, I would like to practice all the skills to extract entities and intents for a given message.
# NLP BASICS
## 1. RASA
[This is the Rasa tutorial:](https://rasa.com/docs/rasa/user-guide/rasa-tutorial/)

The project is based on rasa_nlu, I created rasa.json to train some sentences people usually use when they ask for music recommendations. I have trained intents including:
  * greet
  * goodbye
  * affirm
  * deny
  * music_search
  * artist_search
  * genre_search
  * latest

The first four intents include no entities, and for the rest, it's hard to extract users' indentities in real practice due to the small amount of data. Thus I combined other methods to do this. However, for intent extraction, this trianing has proved its robustness.
## 2. REGULAR EXPRESSIONS
[This is the document introducing regular expressions](https://docs.python.org/2/library/re.html)

I use regular expressions as the number one back-up plan to extract entities for user messages. Admittedly, we could write a scrapy script and create a database recording tracks, albums and their corresponding artists. But it would be a large database, and sometimes ask the user directly whether they are implying an artist or an album/track is the better choice.

Unlike human language, language processed by the machine has many limitations. For example, when I tell you "I want to know some albums by Wakin Chau", you know that I am looking for the artist Wakin Chau's tracks, not some albums called "Wakin Chau". In other word, I am searching music based on an artist, not an album. 

In most time, when people mention an artist's name, their intent would probably be "artist_search", which means the priority of "artist_search" is higher than that of "music_search". Plus, "...by..." is a critical word that could indicate that the user is suggesting an "artist_search".
## 3. SPACY
[This is the official document for SPACY](https://spacy.io/api/doc)

In the third part "genre_search", I use doc.ents in spacy to help me find which genre the user is asking for. For example, when the user enters "I wanna find some music for my brother's wedding", doc.ents will examine each word one by one and see if there is a matchable music genre. Apparently, in this case, we get the answer--"wedding". Then we call a function to obtain a playlist of "wedding" genre.

The complete script is complete.py in the folder Spotify with other test scripts.

# PIC DISPLAY
The chat is something looks like this:
![Alt text](https://github.com/Georgeanna-Li/Anna_music_Recommendation/blob/master/art/pic1.png)

The bot will return a list of tracks in an album:
![Alt text](https://github.com/Georgeanna-Li/Anna_music_Recommendation/blob/master/art/pic2.png)

# SPOTIFY&SPOTIPY
As we all know, SPOTIFY is one of the most popular music players in the world.You can get your spotify developer token from here [SPOTIFY DEVELOPER](https://developer.spotify.com/dashboard/login)

However, there is another module in Python called Spotipy which offers more friendly-written API, thus I choose this module to build my chatbot.
Once you have logged in spofify developer, pass your client_id and client_secret into the terminal like this:
```
export SPOTIPY_CLIENT_ID=your_client_id
export SPOTIPY_CLIENT_SECRET=your_client_secret
```
In your python script, install module Spotipy, and pass the credentials:
```
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
```
```
client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
```
# FACEBOOK MESSENGER
Set up a fan page using your FB account, and then add a new application on facebook developer page like this:

# FRONT END
This page introduces a method to host a WebApp without building a server using Pythonanywhere,but I apply a server anyway on Microsoft Azure, thanks to the 200$ free trial for the first month.




