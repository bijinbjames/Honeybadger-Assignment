from flask import Flask, request
import os
import requests
import json
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    payload = request.get_json()
    if payload.get('Type') == 'SpamNotification':
        email = payload.get('Email')
        message = {'text': f"Alert: Spam notification for {email}!"}
        webhook_url = (os.getenv("SLACK_APP_TOKEN"))
        response = requests.post(webhook_url, data=json.dumps(message), headers={'Content-Type': 'application/json'})
        if response.status_code != 200:
            raise ValueError(f'Request to Slack returned an error: {response.status_code}, {response.text}')
    return 'OK'

if __name__ == '__main__':
    app.run(debug=True)
