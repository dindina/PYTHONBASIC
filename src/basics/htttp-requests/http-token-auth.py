import requests

url = "https://api.example.com/protected"
token = "YOUR_API_TOKEN"
headers = {'Authorization': f'Bearer {token}'}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    print(response.json())
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
except requests.exceptions.HTTPError as err:
    print(f"HTTP Error: {err}")