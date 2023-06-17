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

    film_retrieve_view_serializer = serializers.FilmRetrieveViewSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            # process film request view (created new instance of special FilmRetrieveView model if it can be done)
            # not throws errors if can`t write film view instance
            self.film_retrieve_view_serializer.process_film_view(
                request=request,
                film_id=kwargs.get('pk')
            )
        except Exception:
            pass

        return super().retrieve(request, *args, **kwargs)
