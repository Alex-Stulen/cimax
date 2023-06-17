from rest_framework import serializers

from utils.ip import get_client_ip, ip_info
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
    film_view_count = serializers.IntegerField(source='film_retrieve_view_set.count', read_only=True)

    class Meta:
        model = models.Film
        fields = '__all__'


class FilmRetrieveViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FilmRetrieveView
        fields = '__all__'

    @classmethod
    def process_film_view(cls, request, film_id: int):
        ip_address = get_client_ip(request)
        if cls.Meta.model.objects.filter(ip_address=ip_address, film__id=film_id).exists():
            return

        serializer = cls(data={
            'ip_address': ip_address,
            'ip_info': ip_info(ip_address),
            'film': film_id
        })

        is_valid_serializer = serializer.is_valid(raise_exception=True)
        if is_valid_serializer:
            return serializer.save()
