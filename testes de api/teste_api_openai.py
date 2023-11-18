import requests as rq
import json
from dotenv import load_dotenv
import os

load_dotenv()
SECRET_KEY_GPT = os.getenv("SECRET_KEY_GPT")


url = "https://api.openai.com/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + SECRET_KEY_GPT
}
data = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "Say this is a test!"}],
    "temperature": 0.7
}

response = rq.post(url, headers=headers, data=json.dumps(data))

response_json = response.json()

print(response_json)# to sem credito entao outputa nada, mas em geral é pra tar funcionando
