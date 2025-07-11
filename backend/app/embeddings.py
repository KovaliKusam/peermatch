import requests
import json

def get_embedding(text):
    print('Call 2')
    app_id = "sparkassist"
    model = 'text-embedding-3-small'
    api_key = "eyJraWQiOiJMd29kQ04wZFNtbXRlVFpEZG5YUVpxZzBwU3NQLUlUU1JGM19aamgzSWZjIiwiYWxnIjoiUlMyNTYifQ.eyJ2ZXIiOjEsImp0aSI6IkFULkRQQkRFNWUwQmhaTnRHNnJSOHdMRHM0RUs1Qk9tbFJsQmFyaUVJUUg4MGMub2FyM2oydG02aldGc3hhN0k1ZDciLCJpc3MiOiJodHRwczovL3NwZ2xvYmFsLm9rdGEuY29tL29hdXRoMi9kZWZhdWx0IiwiYXVkIjoiYXBpOi8vZGVmYXVsdCIsImlhdCI6MTc1MjE5ODM0NiwiZXhwIjoxNzUyMjAxOTQ2LCJjaWQiOiIwb2Fld3gyeGxudE9jMVFUazVkNyIsInVpZCI6IjAwdXAwZmppeXNWTWIzak9XNWQ3Iiwic2NwIjpbIm9mZmxpbmVfYWNjZXNzIiwicHJvZmlsZSIsImVtYWlsIiwib3BlbmlkIl0sImF1dGhfdGltZSI6MTc1MjEyNzU4NiwiY291bnRyeSI6IklORElBIiwic3ViIjoia292YWxpLmt1c2FtQHNwZ2xvYmFsLmNvbSJ9.BuSi_uU7uMwaYvgiy8NdZ0epefTOXv5GoZ9R0lYI1hTI8cyBuoRKvmOI5hsIzuL6Fd-2L2fpoC77WXYZMTa9xCGhUNfv8bNkdoem7JWCg3NiX7ThSdoYg3GPkelBf_O0pjHW-EZRqqHJSd7Y-vWWQ2jX3Vbm2o4aQye2DRzOW5qvHPOglvvlS1-rIvb00jClBpZbqgBLVbpxIgWIzSJNXd_w2H0RiGc8dHeNuG86oFomSDXqol3NPTX0-H9MegEP1K_BnVuo-MWaGCWVphQ9k45_U4llltOSHToci1XDoF1K0ItYze0ISzfPqF7JZ6MqatNMrV2Hqm4N9OK4zb-FOQ"  # Use environment variable for security
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