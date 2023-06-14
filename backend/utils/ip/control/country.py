from django.conf import settings

from utils.ip import get_client_ip, ip_info


def is_allowed_request_ip_country(request):
    try:
        request_ip = get_client_ip(request)
        request_ip_info = ip_info(request_ip)
        request_ip_country = request_ip_info.get('country', '')

        # True if IP in allowed countries, else False
        return request_ip_country in settings.ALLOWED_CLIENT_COUNTRIES
    except Exception as e:
        return False
