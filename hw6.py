import os
import base64
import requests
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
auth_key = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()

headers = {"Authorization": f"Basic {auth_key}"}
data = {
    "grant_type": "client_credentials",
}
response = requests.post(
    "https://accounts.spotify.com/api/token",
    headers=headers,
    data=data,
)
auth_token = response.json()['access_token']

top_songs_response = requests.get(
    "https://api.spotify.com/v1/browse/new-releases",
    headers={"Authorization": f"Bearer {auth_token}"}
)

for item in top_songs_response.json()["albums"]["items"]:
    print(item["name"])
