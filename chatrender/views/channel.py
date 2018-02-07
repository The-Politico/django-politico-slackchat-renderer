from urllib.parse import urljoin

import requests

from chatrender.conf import settings
from django.shortcuts import render

CHANNEL_API_URI = urljoin(settings.SERIALIZER_API_URL, 'channel/')


def channel(request, chat_type):
    response = requests.get(CHANNEL_API_URI)
    context = response.json()
    return render(
        request,
        'chatrender/channel_list.html',
        context={"channels": context, "chat_type": chat_type}
    )
