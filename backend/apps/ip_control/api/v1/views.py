from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response


class IpControlAccessApiView(APIView):
    # main logic processed in middleware
    def get(self, request: Request) -> Response:
        """ Returns status 200 if ip is allowed or returns status 403 if ip is not allowed """
        return Response(status=status.HTTP_200_OK)
