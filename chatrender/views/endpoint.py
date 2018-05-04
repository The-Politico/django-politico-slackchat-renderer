from chatrender.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class Endpoint(APIView):
    # Open API
    authentication_classes = ()
    permission_classes = ()

    valid_request_types = [
        'url_verification',
        'update_notification',
        'republish_request',
    ]

    def post(self, request, *args, **kwargs):
        from chatrender.celery import publish_slackchat

        data = request.data
        request_token = data.get('token', None)
        request_type = data.get('type', None)

        if request_token != settings.WEBHOOK_VERIFICATION_TOKEN:
            return Response(status=status.HTTP_403_FORBIDDEN)

        if request_type not in self.valid_request_types:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if request_type == 'url_verification':
            return Response(
                data=data.get('challenge'),
                status=status.HTTP_200_OK
            )

        try:
            channel = data.get('channel')
            chat_type = data.get('chat_type')
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if request_type == 'update_notification':
            publish_slackchat.delay(chat_type, channel)
        if request_type == 'republish_request':
            publish_slackchat.delay(chat_type, channel, statics=True)

        return Response(status=status.HTTP_200_OK)
