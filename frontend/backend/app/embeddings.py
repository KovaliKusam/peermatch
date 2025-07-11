import requests
import json

def get_embedding(text):
    print('Call 2')
    app_id = "sparkassist"
    model = 'text-embedding-3-small'
    api_key = "eyJraWQiOiJMd29kQ04wZFNtbXRlVFpEZG5YUVpxZzBwU3NQLUlUU1JGM19aamgzSWZjIiwiYWxnIjoiUlMyNTYifQ.eyJ2ZXIiOjEsImp0aSI6IkFULldRSS00SFdmc0pQdnZZa0dQdkJTX2k2T1kzaGNKVmtERHg2b3lXcFNMb28ub2FyM2oydG02aldGc3hhN0k1ZDciLCJpc3MiOiJodHRwczovL3NwZ2xvYmFsLm9rdGEuY29tL29hdXRoMi9kZWZhdWx0IiwiYXVkIjoiYXBpOi8vZGVmYXVsdCIsImlhdCI6MTc1MjE3NzU5MCwiZXhwIjoxNzUyMTgxMTkwLCJjaWQiOiIwb2Fld3gyeGxudE9jMVFUazVkNyIsInVpZCI6IjAwdXAwZmppeXNWTWIzak9XNWQ3Iiwic2NwIjpbIm9mZmxpbmVfYWNjZXNzIiwicHJvZmlsZSIsImVtYWlsIiwib3BlbmlkIl0sImF1dGhfdGltZSI6MTc1MjEyNzU4NiwiY291bnRyeSI6IklORElBIiwic3ViIjoia292YWxpLmt1c2FtQHNwZ2xvYmFsLmNvbSJ9.DLGEjpcIsJA-LksTUBLntm8eDPzBSE12GsYSu5pV1rvToqfhZCYdhgXFgAjF_BNzhvT7HW5q2KM8UxO7B19_dWOfgHw3__DwhFRQkAtoIOETTCrhU_OuDUILA4eGS__i4EXNmbVLPH-U3njsqI4-TgudyhVEf-j_-e0DHgAuV_1hCfYPLjxbA5kKGi0RhIU1AlAxiXRJbXaaYEVh7IunQmHsFaxO3LAL1JmwcTJhGgZWD-PepZfzyIV3R1-jMOfVlqlkNNBR7gbX0Z7IvL8Dq6wbUnMvTp7Eg7jzbayvTxsnC15UmiQfSZ5LNP8E9Wx-uYnMCG3gmEeXY0eGMLr2BQ"  # Use environment variable for security
    url = f"https://sparkapi.spglobal.com/v1/{app_id}/openai/deployments/{model}/embeddings?api_version=2024-02-01"
    
    # Prepare the payload
    payload = json.dumps({
        "input": text
    })
    
    # Set the request headers
    headers = {
        'api-key': api_key,
        'Content-Type': 'application/json'
    }
    
    # Log the request details
    print(f"Posting to URL: {url}")
    print(f"Headers: {headers}")
    print(f"Payload: {payload}")
    
    try:
        # Make the POST request with a timeout
        response = requests.post(url, headers=headers, data=payload, timeout=10)
        print('After posting')
        
        # Check the response status
        if response.status_code == 200:
            return response.json()  # Return the JSON response
        else:
            raise Exception(f"Error: {response.status_code}, {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

# Example usage
# if __name__ == "__main__":
#     # Call the function with a sample text
#     try:
#         result = get_embedding("Your sample text here")
#         print("Embedding result:", result)
#     except Exception as e:
#         print("An error occurred:", e)