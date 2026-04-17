import pyrebase
import requests

# YOUR DATA
BOT_TOKEN = "MTQ5NDgyMjI0MTA4OTg4MDIwNQ.GavAeO.Vne4lYUGQDeKwxjXcDInZbrhrOn1FeUI77yAoY"
GUILD_ID = "1494771338571681873" 

config = {
    "apiKey": "AIzaSyC-tWfooosC689hzDUC4S5CXL7dJ3yANuc",
    "authDomain": "neuro-chat-8fe18.firebaseapp.com",
    "databaseURL": "https://neuro-chat-8fe18-default-rtdb.firebaseio.com",
    "projectId": "neuro-chat-8fe18",
    "storageBucket": "neuro-chat-8fe18.firebasestorage.app",
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

def add_to_server(uid, token):
    url = f"https://discord.com/api/v10/guilds/{GUILD_ID}/members/{uid}"
    headers = {"Authorization": f"Bot {BOT_TOKEN}", "Content-Type": "application/json"}
    r = requests.put(url, headers=headers, json={"access_token": token})
    print(f"Result for {uid}: {r.status_code}")

def stream_handler(message):
    if message['data'] and 'access_token' in str(message['data']):
        # If it's a new login, pull them in
        data = message['data']
        if 'id' in data:
            add_to_server(data['id'], data['access_token'])

print("BRIDGE ONLINE - WAITING FOR LOGINS...")
db.child("logins").stream(stream_handler)
