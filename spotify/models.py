from django.db import models


class Image(models.Model):
    url = models.URLField(max_length=500)
    height = models.IntegerField()
    width = models.IntegerField()

    def __str__(self):
        return self.url


class Artist(models.Model):
    spotify_url = models.URLField(max_length=500)
    followers_total = models.IntegerField()
    genres = models.JSONField()
    api_href = models.CharField(max_length=500)
    spotify_id = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    popularity = models.IntegerField()
    uri = models.CharField(max_length=100)
    images = models.ManyToManyField(Image)

    def __str__(self):
        return self.name

