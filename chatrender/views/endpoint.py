from chatrender.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class Endpoint(APIView):
    # Open API
    authentication_classes = ()
    permission_classes = ()

    def post(self, request, *args, **kwargs):
        from chatrender.celery import publish_slackchat

        data = request.data

        if data.get('token', None) != settings.WEBHOOK_VERIFICATION_TOKEN:
            return Response(status=status.HTTP_403_FORBIDDEN)

        if data.get('type', None) == 'url_verification':
            return Response(
                data=data.get('challenge'),
                status=status.HTTP_200_OK
            )

        if data.get('type', None) != 'update_notification':
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            channel = data.get('channel')
            chat_type = data.get('chat_type')
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        publish_slackchat.delay(chat_type, channel)

        return Response(status=status.HTTP_200_OK)
