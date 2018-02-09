import requests

from chatrender.conf import settings
from django.shortcuts import render


def channel(request, chat_type):
    response = requests.get(settings.SLACKCHAT_CHANNEL_ENDPOINT)
    context = response.json()
    return render(
        request,
        'chatrender/channel_list.html',
        context={"channels": context, "chat_type": chat_type}
    )
