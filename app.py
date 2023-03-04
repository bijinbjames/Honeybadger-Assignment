from flask import Flask, request
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    payload = request.get_json()
    if payload.get('Type') == 'SpamNotification':
        email = payload.get('Email')
        message = {'text': f"Alert: Spam notification for {email}!"}
        webhook_url = 'https://hooks.slack.com/services/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'
        response = requests.post(webhook_url, data=json.dumps(message), headers={'Content-Type': 'application/json'})
        if response.status_code != 200:
            raise ValueError(f'Request to Slack returned an error: {response.status_code}, {response.text}')
    return 'OK'

if __name__ == '__main__':
    app.run(debug=True)
