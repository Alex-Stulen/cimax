from django.urls import path, include

app_name = 'api_v1'

urlpatterns = [
    path('simple-films/', include('apps.simple_film.api.urls', namespace='simple_film_api')),
]
