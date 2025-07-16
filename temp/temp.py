import requests
import json

url = "https://sparkdevapi.spglobal.com/v1/sparkassist/openai/deployments/gpt-4o-mini/chat/completions?api_version=2024-02-01"

payload = json.dumps({
  "frequency_penalty": 0,
  "max_tokens": 500,
  "messages": [
    {
      "content": "Answer user's queries",
      "role": "system"
    },
    {
      "content": "what ",
      "role": "user"
    }
  ],
  "n": 1,
  "presence_penalty": 0,
  "stream": "False",
  "temperature": 0.7,
  "top_p": 1,
  "user": "28820" 
})
headers = {
  'accept': 'application/json',
  'api-key': 'eyJraWQiOiJMd29kQ04wZFNtbXRlVFpEZG5YUVpxZzBwU3NQLUlUU1JGM19aamgzSWZjIiwiYWxnIjoiUlMyNTYifQ.eyJ2ZXIiOjEsImp0aSI6IkFULjlaLXlqb0paWWFVSmR4TzVyWEdBWXBsdVJUTVVxWUZmUVlQMHAzMTg1RWMub2FyM2p2amY0dTV3ZjEzTzc1ZDciLCJpc3MiOiJodHRwczovL3NwZ2xvYmFsLm9rdGEuY29tL29hdXRoMi9kZWZhdWx0IiwiYXVkIjoiYXBpOi8vZGVmYXVsdCIsImlhdCI6MTc1MjYzMzA1MiwiZXhwIjoxNzUyNjM2NjUyLCJjaWQiOiIwb2Fld3gyeGxudE9jMVFUazVkNyIsInVpZCI6IjAwdXAwZmppeXNWTWIzak9XNWQ3Iiwic2NwIjpbImVtYWlsIiwib2ZmbGluZV9hY2Nlc3MiLCJvcGVuaWQiLCJwcm9maWxlIl0sImF1dGhfdGltZSI6MTc1MjYyNzYzMCwiY291bnRyeSI6IklORElBIiwic3ViIjoia292YWxpLmt1c2FtQHNwZ2xvYmFsLmNvbSJ9.Ae_kJK9qYSfkV0IAxn60KxA-BT54gYWUdI2-AeY5ZkuLLI_13kq8tem7YY5nwvdSSn6WtgPJ51-cIP5nS0RjBYdToyDxMuYDnxSr-Ok-8RvE3Rf8Tf8fMBsIo3b9CD3BYU_r0owlnvW-yPcB1paEPJhVTkZ71CD1Zd0oTC2XyHubwRZ_rwomC1kd0e1GD2IGpwFXxrmyJrJZQXf2x9lRmIQm24aIrFJ8PPiNGD0NuP9rnjsHr4InLcGpJ-gU0RwIEi7Y3-f21PDGbDmRlMP08BCKFpgFRVU9T2c0WmKzhmrtdxGgbjKfm3_X-m9uHgYR4DasNjDq_NPwMWxZgMT6cw',
  'rag': 'true',
  'incognito': 'false',
  'sparkid': '0',
  'maxchunks': '5',
  'similarity': '0.5',
  'Content-Type': 'application/json',
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

