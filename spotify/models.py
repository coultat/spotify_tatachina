from django.db import models


class Image(models.Model):
    url = models.URLField(max_length=500)
    height = models.IntegerField()
    width = models.IntegerField()

    def __str__(self):
        return self.url


def default_genres() -> list[str]:
    return ["modern-music", "trap"]


class Artist(models.Model):
    spotify_url = models.URLField(max_length=500)
    followers_total = models.IntegerField(default=0)
    genres = models.JSONField(default=default_genres)
    api_href = models.CharField(max_length=500, default="no api_href")
    spotify_id = models.CharField(max_length=50, default="Unknown Id")
    name = models.CharField(max_length=200, default="Unknown Artist")
    popularity = models.IntegerField(default=0)
    uri = models.CharField(max_length=100, default="Unknown Uri")
    images = models.ManyToManyField(Image)