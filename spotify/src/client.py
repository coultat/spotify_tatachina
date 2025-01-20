import base64
import logging
import httpx
from spotify.src.utils import env
from rest_framework import response


class SpotifyClient:
    def __init__(self) -> None:
        self.client_id = env("SPOTIFY_CLIENT_ID")
        self.client_secret = env("SPOTIFY_CLIENT_SECRET")
        self.auth_url = env("SPOTIFY_AUTH_URL")
        self.artist_url = env("SPOTIFY_ARTIST_URL")
        self.playlist_url = env("SPOTIFY_PLAYLIST_URL")
        self.timeout = 2.00
        self.headers = self.get_authorization()

    def get_token(self) -> str:
        auth_header = base64.b64encode(
            f"{self.client_id}:{self.client_secret}".encode()
        ).decode()
        headers = {"Authorization": f"Basic {auth_header}"}
        data = {"grant_type": "client_credentials"}
        try:
            response = httpx.post(
                self.auth_url, headers=headers, data=data, timeout=self.timeout
            )
            response.raise_for_status()
            return response.json()["access_token"]
        except httpx.HTTPStatusError as err:
            message_log = (
                f"Unable to connect to external service. Check credentials {err=}"
            )
            logging.exception(message_log)
            raise httpx.HTTPStatusError(
                message="Unable to perform client request",
                request=err.request,
                response=err.response,
            ) from err
        except httpx.TimeoutException as err:
            message = f"Error with external service {err=}"
            logging.exception(message)
            raise httpx.TimeoutException(message=message) from err

    def get_authorization(self) -> dict[str, str]:
        token = self.get_token()
        return {"Authorization": f"Bearer {token}"}

    async def get_artist(self, artist_id: str) -> response:
        return httpx.get(
            self.artist_url + artist_id, headers=self.headers, timeout=self.timeout
        )
