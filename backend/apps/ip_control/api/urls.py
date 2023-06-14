from django.urls import path, include

app_name = 'ip_control_api'

urlpatterns = [
    path('', include('apps.ip_control.api.v1.urls')),
]
