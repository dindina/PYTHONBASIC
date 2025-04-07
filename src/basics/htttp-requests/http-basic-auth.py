import requests
from requests.auth import HTTPBasicAuth

url = "https://httpbin.org/basic-auth/user/passwd"
auth = HTTPBasicAuth('user', 'passwd')

try:
    response = requests.get(url, auth=auth)
    response.raise_for_status()
    print("Authentication successful!")
    print(response.json())
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
except requests.exceptions.HTTPError as err:
    print(f"HTTP Error: {err}")