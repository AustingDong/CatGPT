import requests
import time
def tts_vits(text, language):
    response = requests.post(url='http://127.0.0.1:8001/tts', json={"text": text, "language": language})
    if response.status_code == 200:
        with open('./result/tts_vits.wav', 'wb') as f:
            f.write(response.content)
            f.close()
            
    else:
        print(f"Request failed with status code {response.status_code}")