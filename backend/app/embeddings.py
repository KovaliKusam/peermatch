import requests
import json

def get_embedding(text):
    print('Call 2')
    app_id = "sparkassist"
    model = 'text-embedding-3-small'
    api_key = "eyJraWQiOiJMd29kQ04wZFNtbXRlVFpEZG5YUVpxZzBwU3NQLUlUU1JGM19aamgzSWZjIiwiYWxnIjoiUlMyNTYifQ.eyJ2ZXIiOjEsImp0aSI6IkFULmhmWXIxem1QRHFMSEVvRTNmMjFzVUl6WFQ4Z1k0d3daRjNhSndsLU54Yk0ub2FyM2pqbnA3ekc5OE5EaVg1ZDciLCJpc3MiOiJodHRwczovL3NwZ2xvYmFsLm9rdGEuY29tL29hdXRoMi9kZWZhdWx0IiwiYXVkIjoiYXBpOi8vZGVmYXVsdCIsImlhdCI6MTc1MjQ1NTM1MSwiZXhwIjoxNzUyNDU4OTUxLCJjaWQiOiIwb2Fld3gyeGxudE9jMVFUazVkNyIsInVpZCI6IjAwdXAwZmppeXNWTWIzak9XNWQ3Iiwic2NwIjpbIm9wZW5pZCIsInByb2ZpbGUiLCJvZmZsaW5lX2FjY2VzcyIsImVtYWlsIl0sImF1dGhfdGltZSI6MTc1MjQ1NTM0OSwiY291bnRyeSI6IklORElBIiwic3ViIjoia292YWxpLmt1c2FtQHNwZ2xvYmFsLmNvbSJ9.S_p6Gk_LTnd2TQIlAvpO6d1p2EwSwUnULU2saWLJ4jQLjHMjivaRRZjCOST0XL6UUwbPOCmTArASbDvVOGzaVml5wpHnrr6FXJ_4pqavD7TMhtIdm6nGnrQiZMYDGtBROZJH6aO7Y5NB0I0N8iuz-eaBBtHjg2RBZGnX66NEGLK1uUSEb968A35gGpkyfFDu_hq9TYbeE_AS_3TKYuxxmNxtuQnNsJocdWAvz2mWLAtZ26E1-4OrVjlaKmf9upCZT0uDGab55-uwdG6VtETe9oAGfJyvssJ4Je-MQF9JOhvx8JqLAoKlV_WYgUoW6_tK2ZzJkWkIL1zEMBeCxbCm9w"  # Use environment variable for security
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