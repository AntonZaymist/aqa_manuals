import json
import requests
from requests import codes


response = requests.get("https://api.github.com")
print(response.status_code)
# assert response.status_code == 200, f"Failed to request. Response: {response}"
assert response.status_code == requests.codes.ok, f"Failed to request. Response: {response}"
response.json()
print(json.loads(response.text))
# print(response.content)
# print(response.json())
# print(response.headers)