from typing import Any, ClassVar, Self, Union

from rest_framework import serializers

from .models import Artist, Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields: ClassVar[list[str]] = ["url", "height", "width"]


class ArtistSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)

    class Meta:
        model = Artist
        fields: ClassVar[list[str]] = [
            "spotify_url",
            "followers_total",
            "genres",
            "api_href",
            "spotify_id",
            "name",
            "popularity",
            "uri",
            "images",
        ]

    def to_internal_value(self: Self, data: dict[str, Union[str, int, dict[str, str]]]):
        data = {
            "spotify_url": data.get("external_urls", {}).get("spotify"),
            "followers": data.get("followers", {}).get("total"),
            "genres": data.get("genres"),
            "api_href": data.get("href"),
            "spotify_id": data.get("id"),
            "name": data.get("name"),
            "popularity": data.get("popularity"),
            "uri": data.get("uri"),
            "images": data.get("images"),
        }
        return super().to_internal_value(data)

    def create(self, validated_data: dict[str, Any]) -> Artist:
        images_data = validated_data.pop("images")
        artist = Artist.objects.create(**validated_data)

        for image_data in images_data:
            image = Image.objects.create(**image_data)  # Todo adjust this
            artist.images.add(image)

        return artist
