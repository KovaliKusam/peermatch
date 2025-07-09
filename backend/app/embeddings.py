import requests
import json

def get_embedding(text):
    app_id = "sparkassist"
    model='text-embedding-3-large'
    api_key = "eyJraWQiOiJMd29kQ04wZFNtbXRlVFpEZG5YUVpxZzBwU3NQLUlUU1JGM19aamgzSWZjIiwiYWxnIjoiUlMyNTYifQ.eyJ2ZXIiOjEsImp0aSI6IkFULl91U0xLNm5rUnN0YjliUjJrVkdKOER2aWVQNjU5eEg2WEpIUVYyb1BETFEub2FyM2l3cjcxY0R6aDZNb0w1ZDciLCJpc3MiOiJodHRwczovL3NwZ2xvYmFsLm9rdGEuY29tL29hdXRoMi9kZWZhdWx0IiwiYXVkIjoiYXBpOi8vZGVmYXVsdCIsImlhdCI6MTc1MjA2MjM1MiwiZXhwIjoxNzUyMDY1OTUyLCJjaWQiOiIwb2Fld3gyeGxudE9jMVFUazVkNyIsInVpZCI6IjAwdXAwZmppeXNWTWIzak9XNWQ3Iiwic2NwIjpbIm9mZmxpbmVfYWNjZXNzIiwicHJvZmlsZSIsImVtYWlsIiwib3BlbmlkIl0sImF1dGhfdGltZSI6MTc1MjAzNzA2MSwiY291bnRyeSI6IklORElBIiwic3ViIjoia292YWxpLmt1c2FtQHNwZ2xvYmFsLmNvbSJ9.Z2FZyulXgZ6c2e280GPY-3RAJQmUvO4fJH8zH7G4ScHxOD1ORXYfVb9UtwUUPZLRGP09r6dflaBqJd27d6UGpAMCgKEcu1OkDf7b58lSQdpY6O47HUGRj2y9ilCPnV7Dy8l2kHEeemkUx-jDQivhCnfFa9xqhbf0dLC5AFMOHiCksz5eXUp5yhgpXwBGEI5nfGI8v1MOAWv9ccqs2heJX54Pi8n4cm2inu6n6M24l6QrdjIBS-sFQ8TBkebeU4QyEtY1nRjrAzp1uSqNE93qSDVIhLcLE-ocqGEYPC96hN6C6YtfTt6tem0DxFJs0K2plNmCmq2cMK6fSYmNkOrpVg" 
    url = f"https://sparkapi.spglobal.com/v1/{app_id}/openai/deployments/{model}/embeddings?api_version=2024-02-01"
    
    payload = json.dumps({
        "input": text
    })
    
    headers = {
        'api-key': api_key,
        'Content-Type': 'application/json'
    }
    
    response = requests.post(url, headers=headers, data=payload)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error: {response.status_code}, {response.text}")