from rest_framework import routers

from . import views

app_name = 'simple_film_api_v1'

v1_router = routers.DefaultRouter()
urlpatterns = []

v1_router.register('', views.FilmReadOnlyModelViewSet, basename='films')

urlpatterns += v1_router.urls
