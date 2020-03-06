# Anna_music_Recommendation
A project for NLP, a chatbot linked to Facebook fan page to recommend music based on users' requirements

# PURPOSE
Recently I began learning about NLP, and here is a chatbot I built to recommend music.
Since I am a total green hand on this, I first build a bot that I can talk to on my Mac terminal, then I linked it with a FB fan page I created to intilize my bot.
There are a number of changes commited when I am transplanting my python code to the Messenger bot, so I will upload two versions of code. For orinal python code, see the file spotify_github.py; for latter version, see webhook.py.

Since I am learning NLP, I would like to practice all the skills to extract entities and intents for a given message.
## 1. RASA
[Rasa tutorial:](https://rasa.com/docs/rasa/user-guide/rasa-tutorial/)
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

# PIC DISPLAY
The chat is something looks like this:
![Alt text](https://github.com/Georgeanna-Li/Anna_music_Recommendation/blob/master/pic1.png)

The bot will return a list of tracks in an album:
![Alt text](https://github.com/Georgeanna-Li/Anna_music_Recommendation/blob/master/pic2.png)


