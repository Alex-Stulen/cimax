from django.conf import settings
from django.http.response import HttpResponse
from django.utils.deprecation import MiddlewareMixin

from utils.ip.control.country import is_allowed_request_ip_country

__all__ = (
    'RequestIpControlMiddleware',
)


class RequestIpControlMiddleware(MiddlewareMixin):

    def process_request(self, request):
        control_ip_with_debug_mode = getattr(settings, 'CONTROL_IP_WITH_DEBUG_MODE', False)

        # if production mode or debug mode and control with debug mode
        if not settings.DEBUG or (control_ip_with_debug_mode and settings.DEBUG):
            try:
                if not is_allowed_request_ip_country(request):
                    return HttpResponse(status=403)
            except Exception as e:
                return HttpResponse(status=403)