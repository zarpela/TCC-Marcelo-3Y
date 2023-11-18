import requests as rq
import json

url = "https://api.openai.com/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer CENSURADO"
}
data = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "Say this is a test!"}],
    "temperature": 0.7
}

response = rq.post(url, headers=headers, data=json.dumps(data))

response_json = response.json()

print(response_json)
