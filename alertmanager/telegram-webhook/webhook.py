from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')

@app.route('/alert', methods=['POST'])
def send_alert():
    data = request.json
    
    for alert in data.get('alerts', []):
        message = f"""
🚨 Alert: {alert.get('labels', {}).get('alertname', 'Unknown')}
Status: {alert.get('status', 'firing')}
{alert.get('annotations', {}).get('summary', '')}
{alert.get('annotations', {}).get('description', '')}
        """
        
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        requests.post(url, json={
            'chat_id': CHAT_ID,
            'text': message,
            'parse_mode': 'HTML'
        })
    
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)