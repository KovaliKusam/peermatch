import requests
import json

def get_embedding(text):
    print('Call 2')
    app_id = "sparkassist"
    model = 'text-embedding-3-small'
    api_key = "eyJraWQiOiJMd29kQ04wZFNtbXRlVFpEZG5YUVpxZzBwU3NQLUlUU1JGM19aamgzSWZjIiwiYWxnIjoiUlMyNTYifQ.eyJ2ZXIiOjEsImp0aSI6IkFULnRGOXZDYWRtYndHbVhpb0ZlNVk2bnMyRXhsQXBySVRiZTJ3S2hOeE9fek0ub2FyM2oydG02aldGc3hhN0k1ZDciLCJpc3MiOiJodHRwczovL3NwZ2xvYmFsLm9rdGEuY29tL29hdXRoMi9kZWZhdWx0IiwiYXVkIjoiYXBpOi8vZGVmYXVsdCIsImlhdCI6MTc1MjI0NDk2NiwiZXhwIjoxNzUyMjQ4NTY2LCJjaWQiOiIwb2Fld3gyeGxudE9jMVFUazVkNyIsInVpZCI6IjAwdXAwZmppeXNWTWIzak9XNWQ3Iiwic2NwIjpbIm9wZW5pZCIsIm9mZmxpbmVfYWNjZXNzIiwicHJvZmlsZSIsImVtYWlsIl0sImF1dGhfdGltZSI6MTc1MjEyNzU4NiwiY291bnRyeSI6IklORElBIiwic3ViIjoia292YWxpLmt1c2FtQHNwZ2xvYmFsLmNvbSJ9.gydrtCYuHLAFKX3Z59-PHBvWe4iqUEMnuxDlZFD7LCVvCwGT8KXM1ScDLRV2DJt5OLgRyDQvlL89xaSgMDAh9h_mU3tgud725yyyQhuUgIFXKmMcv12Evg8yJVKZAV_hDy4tPCA4AJOpfCml_83lGrCpw4Kt_46xH1gbSY6XgXkpU_oUtyxpf6MQbLAhBGagMSXGsrZeFBXThJiN_0gsPpbTMrDjLrCwNasjiDorG1P9o7vTtLluH8FGi_nofOBX1lsesjAZIwjsKgS_pyZBE1OyxUEHkRw3dOEK3-ilSEFMUYt7uW7L2NRLZnsAB1AsgHUcHmECa0XuBPSzDiKaIQ"  # Use environment variable for security
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