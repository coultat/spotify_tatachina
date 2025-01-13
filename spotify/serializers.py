from rest_framework import serializers
from .models import Artist, Image

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['url', 'height', 'width']

class ArtistSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)

    class Meta:
        model = Artist
        fields = [
            'spotify_url', 'followers_total', 'genres', 'api_href',
            'spotify_id', 'name', 'popularity', 'uri', 'images'
        ]

    def create(self, validated_data):
        images_data = validated_data.pop('images')
        artist = Artist.objects.create(**validated_data)

        for image_data in images_data:
            image = Image.objects.create(**image_data)
            artist.images.add(image)

        return artist
