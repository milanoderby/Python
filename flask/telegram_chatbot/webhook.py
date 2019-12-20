from decouple import config
import requests

token = config('TELEGRAM_BOT_TOKEN')
url = "https://api.telegram.org/bot"
ngrok_url = "https://cca4ba97.ngrok.io/write"

data = requests.get(f'{url}{token}/setWebhook?url={ngrok_url}/{token}')
# requests 모듈과 Telegram API의 setWebhook를 이용하여 우리의 원래 URL을 NGROK URL과 연결한다.

print(data)