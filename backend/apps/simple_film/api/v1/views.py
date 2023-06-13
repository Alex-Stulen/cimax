from rest_framework import filters
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.pagination import PageNumberPagination

from apps.simple_film import models

from . import serializers


class FilmPagination(PageNumberPagination):
    page_size = 25
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 100


class FilmReadOnlyModelViewSet(ReadOnlyModelViewSet):
    queryset = models.Film.objects.all()
    serializer_class = serializers.FilmSerializer

    pagination_class = FilmPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'original_name', 'film_year']
