from urllib.parse import urljoin

import requests

from chatrender.conf import settings
from django.shortcuts import render

CHANNEL_API_URI = urljoin(settings.SERIALIZER_API_URL, 'channel/')


def develop(request, chat_type, channel):
    channel_uri = urljoin(CHANNEL_API_URI, channel)
    response = requests.get(channel_uri)
    context = response.json()
    return render(
        request,
        'chatrender/{}/index.html'.format(chat_type),
        context={
            "channel": context,
            "channel_uri": channel_uri,
            "develop": True,
        }
    )
