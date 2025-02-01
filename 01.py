import os
import time
import requests
from dotenv import load_dotenv

load_dotenv('secrets.env')
TOKEN = os.getenv('TOKEN') or 'YOUR_TELEGRAM_BOT_TOKEN'
CHANNEL_ID = os.getenv('CHANNEL_ID') or 'YOUR_CHANNEL_ID'
IMAGE_PATH = 'image.png'

def send_image():
    if not TOKEN or not CHANNEL_ID:
        print("Error: TOKEN or CHANNEL_ID is missing.")
        return
    
    url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
    with open(IMAGE_PATH, 'rb') as image_file:
        files = {'photo': image_file}
        data = {'chat_id': CHANNEL_ID}

        try:
            response = requests.post(url, data=data, files=files)
            if response.status_code == 200:
                print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - success")
            else:
                print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Error: {response.text}")
        except Exception as e:
            print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Network Error: {e}")

if __name__ == '__main__':
    while True:
        send_image()
        time.sleep(86400)

