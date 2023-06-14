import json
from urllib import request as urllib_request


__all__ = (
    'get_client_ip',
    'ip_info'
)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def ip_info(ip: str) -> dict:
    url = f'https://ipinfo.io/{ip}/json'
    response = urllib_request.urlopen(url)
    return json.load(response)
