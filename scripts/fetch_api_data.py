import requests
import json

URL = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(URL)

data = response.json()

with open("data/raw/posts.json", "w") as file:
    json.dump(data, file, indent=4)

print("Raw data saved successfully!")