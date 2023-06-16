from rest_framework import serializers

from apps.simple_film import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'


class FilmConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FilmConfig
        fields = '__all__'


class FilmImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FilmImage
        fields = '__all__'


class FilmSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    config = FilmConfigSerializer()
    images = FilmImageSerializer(source='film_images_set.all', many=True, read_only=True)

    class Meta:
        model = models.Film
        fields = '__all__'
