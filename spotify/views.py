from django.shortcuts import render

# Create your views here.
# from spotify.serializers import ArtistSerializer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from spotify.src.client import SpotifyClient
from spotify.models import Image, Artist
from spotify.db_operations import save_artist_to_db


@api_view(http_method_names=["GET"])
def homepage(request: Request):
    response = {"message": "If you are reading this, you may begin listening to the violins"}
    return Response(data=response,
                    status=status.HTTP_200_OK)


@api_view(http_method_names=["GET"])
def get_artist(request: Request):
    artist_id = request.data['artist_id']
    artist = SpotifyClient().get_artist(artist_id)
    save_artist_to_db(artist)
    # small = Artist.objects.create(
    #     spotify_url=artist.json()['external_urls']['spotify'],
    #     followers_total=artist.json()['followers']['total'],
    #     genres=artist.json()["genres"],
    #     api_href=artist.json()["href"],
    #     spotify_id=artist.json()["id"],
    #     name=artist.json()["name"],
    #     popularity=artist.json()["popularity"],
    #     uri=artist.json()["uri"]
    # )
    #
    # for img in artist.json()["images"]:
    #     image = Image.objects.create(url=img["url"], height=img["height"], width=img["width"])
    #     small.images.add(image)
    #
    # small.save()


    return Response(data=artist,
                    status=status.HTTP_200_OK)


@api_view(http_method_names=["GET"])
def get_parameters(request: Request):
    data = request.data.query_params
    return Response(data=data,
                    status=status.HTTP_200_OK)
