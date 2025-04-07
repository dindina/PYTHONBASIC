import requests

url = "https://www.example.com"

try:
    response = requests.get(url)
    response.raise_for_status()

    print("Response Headers:")
    for key, value in response.headers.items():
        print(f"{key}: {value}")

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
except requests.exceptions.HTTPError as err:
    print(f"HTTP Error: {err}")