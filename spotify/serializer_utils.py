from typing import Any

from spotify.serializers import ArtistSerializer


def prepare_artist(artist_data: dict[str, Any]) -> None:
    return ArtistSerializer(
        data={
            "spotify_url": artist_data["external_urls"]["spotify"],
            "followers_total": artist_data["followers"]["total"],
            "genres": artist_data["genres"],
            "api_href": artist_data["href"],
            "spotify_id": artist_data["id"],
            "name": artist_data["name"],
            "popularity": artist_data["popularity"],
            "uri": artist_data["uri"],
            "images": artist_data["images"],
        }
    )
