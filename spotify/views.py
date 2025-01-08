from django.shortcuts import render

# Create your views here.


from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(http_method_names=["GET"])
def homepage(request: Request):
    response = {"message": "If you are reading this, you may begin listening to the violins"}
    return Response(data=response,
                    status=status.HTTP_200_OK)
