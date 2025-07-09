import requests

SPARKASSIST_URL = "https://sparkuatapi.spglobal.com/sparkassist/embedding/sparkassist/text-embedding-3-small"

HEADERS = {
    "api-key": "<YOUR_OKTA_TOKEN>",  # replace this dynamically if needed
    "Content-Type": "application/json"
}

def get_embedding(text: str):
    payload = {
        "input": text  # for embeddings, it's usually just 'input'
    }
    response = requests.post(SPARKASSIST_URL, headers=HEADERS, json=payload)
    response.raise_for_status()
    return response.json()["data"][0]["embedding"]  # Adjust based on response schema
