import requests as Httprequest
import json

url = "https://jsonplaceholder.typicode.com/posts"
payload = {
    "userId": 1,
    "title": "My New Post",
    "body": "This is the content of my new post."
}
headers = {'Content-Type': 'application/json'}

try:
    response = Httprequest.post(url,headers=headers,data=json.dumps(payload))
    response.raise_for_status()
    print(response.status_code)    
    print(response.json())    
    
except Httprequest.exceptions.HTTPError as e:
    print(f"Http Error {e}")
