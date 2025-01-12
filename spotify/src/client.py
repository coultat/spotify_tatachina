import os
from pathlib import Path
from dotenv import load_dotenv
import base64
import requests
# from spotify.models import Artist


path = Path(__file__).parent.parent.parent / "default.env"
load_dotenv(path)


class SpotifyClient:
    def __init__(self):
        self.client_id = os.getenv("SPOTIFY_CLIENT_ID")
        self.client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
        self.auth_url = os.getenv("SPOTIFY_AUTH_URL")
        self.artist_url = os.getenv("SPOTIFY_ARTIST_URL")
        self.headers = self.get_authorization()

    def get_token(self) -> str:
        auth_header = base64.b64encode(f"{self.client_id}:{self.client_secret}".encode()).decode()
        headers = {'Authorization': f'Basic {auth_header}'}
        data = {"grant_type": "client_credentials"}
        token = requests.post(self.auth_url,  # Todo create exceptions for this 404...
                              headers=headers,
                              data=data)
        return token.json()['access_token']

    def get_authorization(self):
        token = self.get_token()
        return {'Authorization': f'Bearer {token}'}

    def get_artist(self, artist_id: str) :  # Todo craete artist model
        artist = requests.get(self.artist_url + artist_id, headers=self.headers)
        return artist
