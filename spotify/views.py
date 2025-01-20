from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from spotify.models import Artist
from httpx import HTTPStatusError, TimeoutException
from spotify.serializers import ArtistSerializer
from spotify.src.client import SpotifyClient
from spotify.serializer_utils import prepare_artist
import asyncio


@api_view(http_method_names=["GET"])
def homepage() -> Response:
    response = {
        "message": "If you are reading this, you may begin listening to the violins"
    }
    return Response(data=response, status=status.HTTP_200_OK)


@api_view(http_method_names=["GET"])
def get_artist(request: Request) -> Response:
    artist_id = request.data["artist_id"]
    db_artist_id = artist_id.split("?")[0]
    if result := Artist.objects.filter(spotify_id=db_artist_id).first():  # get / filter
        artist = ArtistSerializer(result)
        return Response(data=artist.data, status=status.HTTP_200_OK)
    try:
        result = asyncio.run(SpotifyClient().get_artist(artist_id))
        result.raise_for_status()
        artist = prepare_artist(result.json())
        if artist.is_valid():
            artist.save()
            return Response(data={"result": result.json()}, status=status.HTTP_200_OK)
        return Response(
            data={"error": f"Validation Error {artist.errors}"},
            status=status.HTTP_409_CONFLICT,
        )
    except TimeoutException as err:
        return Response(
            data={"error": f"Connection Timeout when requesting external data {err=}"},
            status=status.HTTP_503_SERVICE_UNAVAILABLE,
        )
    except HTTPStatusError as err:
        return Response(
            data={"error": f"{err.args=}"}, status=status.HTTP_400_BAD_REQUEST
        )
