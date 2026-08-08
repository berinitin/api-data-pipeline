import requests

def fetch_api_data(url):
    try:
        response = requests.get(url, timeout=10)

        response.raise_for_status()

        data = response.json()

    except Exception as e:
        print(f"API Error: {e}")
        return None

    return data

url = "https://jsonplaceholder.typicode.com/posts"

data = fetch_api_data(url)

print(type(data))
