from flask import Flask, render_template, request
from decouple import config
import requests, random

app = Flask(__name__)

url = "https://api.telegram.org/bot"
token = config('TELEGRAM_BOT_TOKEN')
chat_id = config('CHAT_ID')

@app.route('/')
def hello():
    return 'Hello World'

@app.route('/send')
def send():
    text = request.args.get('text')
    requests.get(f'{url}{token}/sendMessage?chat_id={chat_id}&text={text}')
    return render_template('send.html', text=text)

@app.route('/write')
def write():
    return render_template('write.html')

@app.route(f'/{token}', methods=["POST"])
def telegram():
    data = request.get_json()
    text = data['message']['text']
    chatID = data['message']['chat']['id']
    if(text == "안녕"):
        return_text = "안녕하세요."
    elif text=="로또":
        numbers = range(1, 46)
        number = random.sample(numbers, 6)
        return_text = sorted(number)
    else:
        return_text = text
    requests.get(f'{url}{token}/sendMessage?chat_id={chatID}&text={return_text}')
    return "ok", 200
    
if __name__==('__main__'):
    app.run(debug=True)