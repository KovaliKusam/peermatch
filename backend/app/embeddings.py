import requests
import json

def get_embedding(text):
    print('Call 2')
    app_id = "sparkassist"
    model = 'text-embedding-3-small'
    api_key = "eyJraWQiOiJMd29kQ04wZFNtbXRlVFpEZG5YUVpxZzBwU3NQLUlUU1JGM19aamgzSWZjIiwiYWxnIjoiUlMyNTYifQ.eyJ2ZXIiOjEsImp0aSI6IkFULlF2M0l4V0R3enU3STM0WkI5WmNiQ2h3MU13WmhQVVJtdXI5UWwwdkdLRlUub2FyM2oydG02aldGc3hhN0k1ZDciLCJpc3MiOiJodHRwczovL3NwZ2xvYmFsLm9rdGEuY29tL29hdXRoMi9kZWZhdWx0IiwiYXVkIjoiYXBpOi8vZGVmYXVsdCIsImlhdCI6MTc1MjI0ODcxMCwiZXhwIjoxNzUyMjUyMzEwLCJjaWQiOiIwb2Fld3gyeGxudE9jMVFUazVkNyIsInVpZCI6IjAwdXAwZmppeXNWTWIzak9XNWQ3Iiwic2NwIjpbIm9mZmxpbmVfYWNjZXNzIiwiZW1haWwiLCJvcGVuaWQiLCJwcm9maWxlIl0sImF1dGhfdGltZSI6MTc1MjEyNzU4NiwiY291bnRyeSI6IklORElBIiwic3ViIjoia292YWxpLmt1c2FtQHNwZ2xvYmFsLmNvbSJ9.Ki9FkDbUIBMKMmoe9qph8BO6XtFDD4nFCMHndLETozzCNAcK8pijEh7k0LcZ4DMkOqKGajqwo5jLv7_poh9aWSN8T3tCKs0i7fsC9wWI_KMHMUntyhxm6VHhsyCM5lg9BklPTsOHTnBhtZZg0TVb_HA7Nx6bZpDKjVhqXY03J5splI2T2-SD4fY3zEJXxm1WY4jNpLpnhYox0m1nqAzIcgrEF3ekXFxNwMk97duMOEWaYG9SEkXT2vaz6Sb6Zhf4owz0VG1VJMf86CzfsJSyO2WseqXxNTgXPU7__Azx2bLG_o-c5wGwsy3GV1Gqen7aJ5WBdSIpQu0a10MugTdmqw"  # Use environment variable for security
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