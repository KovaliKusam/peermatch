import requests
import json

def get_embedding(text):
    print('Call 2')
    app_id = "sparkassist"
    model = 'text-embedding-3-small'
    api_key = "eyJraWQiOiJMd29kQ04wZFNtbXRlVFpEZG5YUVpxZzBwU3NQLUlUU1JGM19aamgzSWZjIiwiYWxnIjoiUlMyNTYifQ.eyJ2ZXIiOjEsImp0aSI6IkFULndIdjZIcGZBYW5TcmRoZEtsdHRNUlhOdFBXcjhyYWtHUzNESDB1UmwwQTQub2FyM2pqbnA3ekc5OE5EaVg1ZDciLCJpc3MiOiJodHRwczovL3NwZ2xvYmFsLm9rdGEuY29tL29hdXRoMi9kZWZhdWx0IiwiYXVkIjoiYXBpOi8vZGVmYXVsdCIsImlhdCI6MTc1MjQ3NTEzOSwiZXhwIjoxNzUyNDc4NzM5LCJjaWQiOiIwb2Fld3gyeGxudE9jMVFUazVkNyIsInVpZCI6IjAwdXAwZmppeXNWTWIzak9XNWQ3Iiwic2NwIjpbIm9mZmxpbmVfYWNjZXNzIiwicHJvZmlsZSIsImVtYWlsIiwib3BlbmlkIl0sImF1dGhfdGltZSI6MTc1MjQ1NTM0OSwiY291bnRyeSI6IklORElBIiwic3ViIjoia292YWxpLmt1c2FtQHNwZ2xvYmFsLmNvbSJ9.PjtwV-oKLvEtp1RTk8OU9ekS9JdkvNYAVNzLStZ-fSYOcrJFx7HwwXFksL8tXsaHTSngVLNZ15bUX-pYkf01Y6IJX58hDGjuMlV4dKm1v4QfMtoy86ADifMl8o4vWX3Wi-cSQNTQgweA0HND5d7QBPQsmrxDOLyzss08E5yMasDo_y3BY_2BQ28PVWAkPNeKIka5CmLmRrt_K8xiJFU0pMMaGOvok7FCTyn0LiiyF41_IZl6zQByUrxzAszSSsaAV3Og30_UGQK6AUTAx76xfCk6W1PGK6CawnrgVp2QHI0pnRKYFA4kZi5Udu7h55MwEtEk2JgrCTzbSSE85MpWrw"  # Use environment variable for security
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