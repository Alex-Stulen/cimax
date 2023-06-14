from django.urls import path

from rest_framework import routers

from . import views

app_name = 'simple_film_api_v1'

v1_router = routers.DefaultRouter()
urlpatterns = [
    path('is-allowed-ip/', views.IpControlAccessApiView.as_view())
]

urlpatterns += v1_router.urls
