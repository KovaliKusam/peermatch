import requests
import json

def get_embedding(text):
    print('Call 2')
    app_id = "sparkassist"
    model = 'text-embedding-3-small'
    api_key = "eyJraWQiOiJMd29kQ04wZFNtbXRlVFpEZG5YUVpxZzBwU3NQLUlUU1JGM19aamgzSWZjIiwiYWxnIjoiUlMyNTYifQ.eyJ2ZXIiOjEsImp0aSI6IkFULnFPX3dkYjFkb1puUUJSN1hWZnlKbVVIdWdoRXMtOUhFMzhLMl92Yk9OQlkub2FyM2oydG02aldGc3hhN0k1ZDciLCJpc3MiOiJodHRwczovL3NwZ2xvYmFsLm9rdGEuY29tL29hdXRoMi9kZWZhdWx0IiwiYXVkIjoiYXBpOi8vZGVmYXVsdCIsImlhdCI6MTc1MjIwMjA3MiwiZXhwIjoxNzUyMjA1NjcyLCJjaWQiOiIwb2Fld3gyeGxudE9jMVFUazVkNyIsInVpZCI6IjAwdXAwZmppeXNWTWIzak9XNWQ3Iiwic2NwIjpbIm9mZmxpbmVfYWNjZXNzIiwiZW1haWwiLCJwcm9maWxlIiwib3BlbmlkIl0sImF1dGhfdGltZSI6MTc1MjEyNzU4NiwiY291bnRyeSI6IklORElBIiwic3ViIjoia292YWxpLmt1c2FtQHNwZ2xvYmFsLmNvbSJ9.A_Gx1lRP3JDKfMHP1GFzdr4lVD7jAwgfaD_QI6KnJ1DpXA5K2adhs6zdz9GYVY5FrCH0hXFEnHeSEgABphsTrBUeXPVD2coS1-TFcCTLVbtj1F3AsQuZ0FDEj1MDacL3cV_UM_pYIX1y7OaD4R_hk0pJyxRar7e2CuJMR15LkiEKEG5JsyFe0wkrnkYVtQcfQNP9rNxCOdoNQV1vwh7r_zk5fM4IS0wdiBVaM4H7AsjTlLRvHjiZdDbCTTLaxppWiUx0OTh0UZLJ6x2yjZ3iB4vzQCSxbhMbYm1RtavpcyDKHbR6I5DOoaqBbJe076_Yudtzrj3BMyjbvbbaOokvsA"  # Use environment variable for security
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