import requests
import json

def get_embedding(text):
    print('Call 2')
    app_id = "sparkassist"
    model = 'text-embedding-3-small'
    api_key = "eyJraWQiOiJMd29kQ04wZFNtbXRlVFpEZG5YUVpxZzBwU3NQLUlUU1JGM19aamgzSWZjIiwiYWxnIjoiUlMyNTYifQ.eyJ2ZXIiOjEsImp0aSI6IkFULmhYcFR2Vk45aWU4WWcxYktUd3Y0cFY0c0NtV095cDI0aFdqYVFzV1FHdTAub2FyM2pqbnA3ekc5OE5EaVg1ZDciLCJpc3MiOiJodHRwczovL3NwZ2xvYmFsLm9rdGEuY29tL29hdXRoMi9kZWZhdWx0IiwiYXVkIjoiYXBpOi8vZGVmYXVsdCIsImlhdCI6MTc1MjQ5MTQyNCwiZXhwIjoxNzUyNDk1MDI0LCJjaWQiOiIwb2Fld3gyeGxudE9jMVFUazVkNyIsInVpZCI6IjAwdXAwZmppeXNWTWIzak9XNWQ3Iiwic2NwIjpbIm9wZW5pZCIsIm9mZmxpbmVfYWNjZXNzIiwicHJvZmlsZSIsImVtYWlsIl0sImF1dGhfdGltZSI6MTc1MjQ1NTM0OSwiY291bnRyeSI6IklORElBIiwic3ViIjoia292YWxpLmt1c2FtQHNwZ2xvYmFsLmNvbSJ9.P5rBiFioFJcWnbTB4WvyZjEf1jx1b8LZvc3uTwM6IJKKUbiPoQFKH6HdCOVRzMquIjen0w0B2gFF6wPGJXSqH8S9NJIvW1MPFIOW-4ss5IEQOOGlxow0glulHYF61tlwt4nHc92UvBTIb6OxPDYfchPZgw6b4Y_W25exZaNbAPvT0H3P_65Li3XOkIk3FQ7RA7BJYE_CY5EN6O-yHF-WueVseMxBtWlOBSZf5ZZ7vhFbXqRceD7eliV57qbOHPABTRCsM423cubeh8fuUuYC_O1QvmBqhsy2AXnTv5QkJAIG28nWR4AJjSbV59gasDyVPXgAqn4ydOsX1_AzWhOVeg"  # Use environment variable for security
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