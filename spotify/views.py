from django.shortcuts import render

# Create your views here.

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from spotify.src.client import SpotifyClient


@api_view(http_method_names=["GET"])
def homepage(request: Request):
    response = {"message": "If you are reading this, you may begin listening to the violins"}
    return Response(data=response,
                    status=status.HTTP_200_OK)


@api_view(http_method_names=["GET"])
def get_artist(request: Request):
    artist_id = request.data['artist_id']
    artist = SpotifyClient().get_artist(artist_id)
    return Response(data=artist,
                    status=status.HTTP_200_OK)


@api_view(http_method_names=["GET"])
def get_parameters(request: Request):
    data = request.data.query_params
    return Response(data=data,
                    status=status.HTTP_200_OK)
