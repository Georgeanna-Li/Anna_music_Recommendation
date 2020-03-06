import os, sys
from flask import Flask, request
from pymessenger import Bot
app = Flask(__name__)
PAGE_ACCESS_TOKEN = "EAADZACVA4gnYBAI4Xbczgvgeeg4rIok1l58sp3JKwGcD4tnLiCZCw0gqdgVv4uYBMZC0lplNJ9uUiaXGo5esoa3nwhZCeg0tbhEqJQJENa7k0qvoQIb49d97GUWDsFesKq3uvas5rqYqMOaE1HUeFZAqQ0NshZCW7l34kMlZCm7YMq5zVhjjVaM"
bot = Bot(PAGE_ACCESS_TOKEN)
@app.route('/', methods=['GET'])


def verify():
 # Webhook verification
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "annamusicrecommendation":
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200
    return "Hello world", 200

@app.route('/', methods=['POST'])

def webhook():
    data = request.get_json()
    log(data)
    if data['object'] == 'page':
        for entry in data['entry']:
            for messaging_event in entry['messaging']:
# IDs
                sender_id = messaging_event['sender']['id']
                recipient_id = messaging_event['recipient']['id']
                if messaging_event.get('message'):
     # Extracting text message
                    if 'text' in messaging_event['message']:
                        messaging_text = messaging_event['message']['text']
                    else:
                        messaging_text = 'no text'
# Echo
                        response = messaging_text
                        bot.send_text_message(sender_id, messaging_text)
                        return "ok", 200
                        
def log(message):
    print(message)
    sys.stdout.flush()
    if __name__ == "__main__":
        app.run(debug = True, port = 530)
