from django.urls import path

from spotify import views

urlpatterns = [
    path("homepage/", views.homepage, name="spotify_home"),
    path("artists/", views.get_artist, name="get_artist"),
]
