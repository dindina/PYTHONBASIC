import requests as httprequest

url = "https://jsonplaceholder.typicode.com/todos/1"

def invokeget(url):
     response = httprequest.get(url)
     response.raise_for_status()     
     print(response.content)
     print(response.status_code)
     data = response.json()  # Parse the JSON response
     print(data)
     print(f"Title: {data['title']}")


invokeget(url)