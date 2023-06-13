from django.urls import path, include

app_name = 'simple_film_api'

urlpatterns = [
    path('', include('apps.simple_film.api.v1.urls')),
]