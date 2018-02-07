from chatrender.celery import render_slackchat
from chatrender.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class Endpoint(APIView):
    def post(self, request, *args, **kwargs):
        payload = request.data

        if payload.get('token', None) != settings.WEBHOOK_VERIFICATION_TOKEN:
            return Response(status=status.HTTP_403_FORBIDDEN)

        if payload.get('type', None) == 'url_verification':
            return Response(
                data=payload.get('challenge'),
                status=status.HTTP_200_OK
            )

        if payload.get('type', None) != 'update_notification':
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            channel = payload.get('channel')
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        render_slackchat.delay(channel)
        return Response(status=status.HTTP_200_OK)
