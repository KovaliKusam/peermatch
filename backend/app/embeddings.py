import requests
import json

def get_embedding(text):
    print('Call 2')
    app_id = "sparkassist"
    model = 'text-embedding-3-large'
    api_key = "eyJraWQiOiJMd29kQ04wZFNtbXRlVFpEZG5YUVpxZzBwU3NQLUlUU1JGM19aamgzSWZjIiwiYWxnIjoiUlMyNTYifQ.eyJ2ZXIiOjEsImp0aSI6IkFULlNiVGtqbHhWQjlBbk9OMG1BOE5SMjR4QUVkME52X0J5SHZteWt2VHpoaW8ub2FyM2p2amY0dTV3ZjEzTzc1ZDciLCJpc3MiOiJodHRwczovL3NwZ2xvYmFsLm9rdGEuY29tL29hdXRoMi9kZWZhdWx0IiwiYXVkIjoiYXBpOi8vZGVmYXVsdCIsImlhdCI6MTc1MjY2MTY4NiwiZXhwIjoxNzUyNjY1Mjg2LCJjaWQiOiIwb2Fld3gyeGxudE9jMVFUazVkNyIsInVpZCI6IjAwdXAwZmppeXNWTWIzak9XNWQ3Iiwic2NwIjpbIm9mZmxpbmVfYWNjZXNzIiwiZW1haWwiLCJwcm9maWxlIiwib3BlbmlkIl0sImF1dGhfdGltZSI6MTc1MjYyNzYzMCwiY291bnRyeSI6IklORElBIiwic3ViIjoia292YWxpLmt1c2FtQHNwZ2xvYmFsLmNvbSJ9.S9fg5pivOlMlrvu0ZD-dVGsg7BVN-Gp51YfDi-PwomVYlAiJA6eBcIoWhnpAow7gjy3hlFOtSrfrvf_7TZwZVprpzb9dp1GRuBfH-S6GsLP3-pVuN2139D3Py--pc7A_gHq8hw9pGU8PZgs5SC0I3ZMym9FfFuFeEwnjMMY2HmRRIVDiu2F7kmsnBapvqcWpRtLNUlUZGLrABTbFsD0dc0nU5WM9DgF2ck1QVhif-q5j_rQSeJTFkid8YN69xlH6qV2qaO_vp2oJGVTYlA9gbufdKkBB0N2jJTCBXsTabaLCwNLocPJNt_zAm-rSHBsYcRisZebIxZ6J4YLmVc94AQ"  # Use environment variable for security
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