import requests

url = "https://api.github.com/search/repositories"
query = "python"
sort = "stars"

params = {'q': query, 'sort': sort}

try:
    response = requests.get(url, params=params)
    response.raise_for_status()

    search_results = response.json()
    print(f"Found {search_results['total_count']} Python repositories sorted by stars.")
    for repo in search_results['items'][:5]:
        print(f"- {repo['name']} by {repo['owner']['login']} (Stars: {repo['stargazers_count']})")

except requests.exceptions.RequestException as e:
    print(f"Error during GET request: {e}")
except requests.exceptions.HTTPError as err:
    print(f"HTTP Error: {err}")