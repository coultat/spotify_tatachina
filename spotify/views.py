from django.shortcuts import render

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from spotify.src.client import SpotifyClient
from spotify.serializer_utils import prepare_artist


@api_view(http_method_names=["GET"])
def homepage(request: Request):
    response = {"message": "If you are reading this, you may begin listening to the violins"}
    return Response(data=response,
                    status=status.HTTP_200_OK)


@api_view(http_method_names=["GET"])
def get_artist(request: Request):
    artist_id = request.data['artist_id']
    result = SpotifyClient().get_artist(artist_id)
    artist_data = result.json()
    artist_serialized = prepare_artist(artist_data)
    if artist_serialized.is_valid():
        artist_serialized.save()

        return Response(data=artist_serialized.data,
                        status=status.HTTP_201_CREATED)
    return Response(data=artist_serialized.errors,
                    status=status.HTTP_400_BAD_REQUEST)


@api_view(http_method_names=["GET"])
def get_parameters(request: Request):
    data = request.data.query_params
    return Response(data=data,
                    status=status.HTTP_200_OK)
