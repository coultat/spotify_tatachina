import base64
import os
from pathlib import Path

import httpx
import environ
from rest_framework import response


ENV_FILE = Path(__file__).parent.parent.parent / "default.env"
env = environ.Env()
environ.Env.read_env(ENV_FILE)


class SpotifyClient:
    def __init__(self) -> None:
        self.client_id = os.getenv("SPOTIFY_CLIENT_ID")
        self.client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
        self.auth_url = os.getenv("SPOTIFY_AUTH_URL")
        self.artist_url = os.getenv("SPOTIFY_ARTIST_URL")
        self.headers = self.get_authorization()

    def get_token(self) -> str:
        auth_header = base64.b64encode(f"{self.client_id}:{self.client_secret}".encode()).decode()
        headers = {"Authorization": f"Basic {auth_header}"}
        data = {"grant_type": "client_credentials"}
        token = httpx.post(
            self.auth_url,  # Todo create exceptions for this 404...
            headers=headers,
            data=data,
        )
        return token.json()["access_token"]

    def get_authorization(self) -> dict[str, str]:
        token = self.get_token()
        return {"Authorization": f"Bearer {token}"}

    def get_artist(self, artist_id: str) -> response:  # Todo craete artist model
        return httpx.get(self.artist_url + artist_id, headers=self.headers)

