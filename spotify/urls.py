from spotify import views
from django.urls import path


urlpatterns = [
    path("homepage/", views.homepage, name="spotify_home"),
    path("artists/", views.get_artist, name="get_artist")
]